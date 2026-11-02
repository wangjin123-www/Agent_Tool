#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
jta_repo —— 取代码到本工具自己的工作区，并准备 CLAUDE.md

隔离原则（用户明确要求）：
  * **完全不碰用户本地的 clone**。一律从 GitLab 重新取到
    <workspace>/repos/<repo>/<branch>@<sha8>/（workspace 默认在工具目录内）。
  * 工作区**没有 .git**（快照目录），因此物理上不可能被 push 回云端。
  * CLAUDE.md 只在本工具工作区生成与复用，绝不推送。

CLAUDE.md 策略：
  * 缓存键 = <project>@<branch>（**不是** sha —— 否则每个 commit 都要重新全量生成，代价过高）。
  * 缓存未命中 → 跑 claude-md-map 全量生成（INIT）。
  * 缓存命中 → 复制进新工作区，再跑 detect-changes 增量刷新。
  * 仓库 .gitignore 里 `**/CLAUDE.md` 被忽略，git 取下来的代码本来就不含它，必须自己生成。

取代码路径：
  主：blobless + sparse 浅克隆（git 已放开 clone/fetch）
  兜底：GitLab archive API（python-gitlab）
"""

from __future__ import annotations

import shutil
import subprocess
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import jta_env as env


# ---------------------------------------------------------------- 凭证


def gitlab_pat() -> Optional[str]:
    """
    从 Windows 凭据管理器取 GitLab PAT（用 git credential fill）。
    config.gitlab.token_source 支持：
      git-credential-manager（默认，不落盘）
      env                   → 读 GITLAB_PAT 环境变量
      file:<path>           → 读一个只含 token 的文件
    绝不把 token 写进任何输出。
    """
    import os

    src = env.cfg_get("gitlab", "token_source", default="git-credential-manager")
    host = env.cfg_get("gitlab", "host", default="https://gitlab.gz.cvte.cn")
    hostname = host.split("://", 1)[-1].rstrip("/")

    if src == "env":
        return os.environ.get("GITLAB_PAT") or None
    if src.startswith("file:"):
        p = Path(src.split(":", 1)[1])
        return p.read_text(encoding="utf-8").strip() if p.exists() else None

    # git credential fill
    try:
        cp = subprocess.run(
            ["git", "credential", "fill"],
            input=f"protocol=https\nhost={hostname}\n\n",
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=60,
            cwd=env.safe_cwd(),
        )
        for line in (cp.stdout or "").splitlines():
            if line.startswith("password="):
                return line.split("=", 1)[1].strip() or None
    except Exception as e:  # noqa: BLE001
        env.log(f"读取 git 凭证失败：{e}")
    return None


def repo_url(project: str) -> str:
    host = env.cfg_get("gitlab", "host", default="https://gitlab.gz.cvte.cn").rstrip("/")
    return f"{host}/{project}.git"


# ---------------------------------------------------------------- 工作区


def repo_dir_name(project: str) -> str:
    return project.rstrip("/").split("/")[-1]


def snapshot_dir(project: str, branch: str, sha8: str) -> Path:
    return env.workspace_root() / "repos" / repo_dir_name(project) / f"{branch}@{sha8}"


def mirror_dir(project: str) -> Path:
    """blobless 浅克隆的持久镜像目录（跨工单复用，只 fetch 增量）。"""
    return env.workspace_root() / "repos" / repo_dir_name(project) / ".mirror"


# ---------------------------------------------------------------- 取代码


def _run_git(args: List[str], cwd: Optional[Path] = None, timeout: int = 1800) -> subprocess.CompletedProcess:
    cp = env.run(["git", *args], cwd=str(cwd) if cwd else env.safe_cwd(), timeout=timeout)
    return cp


def _run_git_binary(args: List[str], cwd: Optional[Path] = None, timeout: int = 1800) -> subprocess.CompletedProcess:
    """
    跑会产出二进制 stdout 的 git 命令（如 git archive --format=tar）。
    env.run 是 text 模式，不适合二进制；这里单开一个 bytes 通道。
    注意仍需中文/编码一致性，故保留 child_env 处理。
    """
    return subprocess.run(
        ["git", *args],
        cwd=str(cwd) if cwd else env.safe_cwd(),
        env=env.child_env(),
        capture_output=True,          # 不加 text → stdout/stderr 是 bytes
        timeout=timeout,
    )


def fetch_via_git(project: str, branch: str, scope: Optional[str]) -> Dict[str, Any]:
    """
    blobless + sparse 浅克隆。
    第一次 clone 到 .mirror，后续 fetch 增量；再 checkout 出 <branch>@<sha8> 快照。
    """
    url = repo_url(project)
    mirror = mirror_dir(project)
    mirror.parent.mkdir(parents=True, exist_ok=True)

    if not (mirror / ".git").exists():
        env.log(f"  首次浅克隆 {project}@{branch} …")
        cp = _run_git([
            "clone", "--filter=blob:none", "--no-checkout", "--depth", "1",
            "--branch", branch, url, str(mirror),
        ])
        if cp.returncode != 0:
            return {"ok": False, "error": f"clone 失败：{(cp.stderr or '')[-800:]}"}
    else:
        env.log(f"  增量 fetch {project}@{branch} …")
        cp = _run_git(["fetch", "--depth", "1", "origin", branch], cwd=mirror)
        if cp.returncode != 0:
            return {"ok": False, "error": f"fetch 失败：{(cp.stderr or '')[-800:]}"}

    # sparse-checkout：只展开 analysis_scope
    if scope:
        cp = _run_git(["sparse-checkout", "init", "--cone"], cwd=mirror)
        cp = _run_git(["sparse-checkout", "set", scope], cwd=mirror)
        if cp.returncode != 0:
            env.log(f"  sparse-checkout 失败（回退全量）：{(cp.stderr or '')[-300:]}")

    # 取 sha 并 checkout
    cp = _run_git(["rev-parse", f"origin/{branch}"], cwd=mirror)
    if cp.returncode != 0:
        # 有些浅克隆场景下只有 FETCH_HEAD
        cp = _run_git(["rev-parse", "FETCH_HEAD"], cwd=mirror)
    if cp.returncode != 0:
        return {"ok": False, "error": f"rev-parse 失败：{(cp.stderr or '')[-400:]}"}
    sha = (cp.stdout or "").strip()
    sha8 = sha[:8]

    snap = snapshot_dir(project, branch, sha8)
    src = snap / "src"
    if src.exists():
        shutil.rmtree(src, ignore_errors=True)
    src.mkdir(parents=True, exist_ok=True)

    env.log(f"  checkout {sha8} → {snap.name}")
    # 用 git archive 从 mirror 导出快照，避免在 mirror 里反复切分支。
    # 走二进制通道，不能经 env.run（text 模式会破坏 tar 字节流）。
    cp = _run_git_binary(["archive", "--format=tar", sha], cwd=mirror)
    if cp.returncode != 0:
        err = (cp.stderr or b"").decode("utf-8", "replace")[-400:]
        return {"ok": False, "error": f"git archive 失败：{err}"}
    payload = cp.stdout or b""
    if not payload:
        return {"ok": False, "error": "git archive 没有输出（可能 sparse 设置把内容全排除了）"}
    import io, tarfile
    with tarfile.open(fileobj=io.BytesIO(payload), mode="r:") as t:
        # 防路径穿越
        for m in t.getmembers():
            if m.name.startswith(("/", "\\")) or ".." in Path(m.name).parts:
                continue
            t.extract(m, src)

    return {"ok": True, "method": "git", "sha": sha, "sha8": sha8,
            "snapshot": str(snap), "src": str(src), "branch": branch, "project": project}


def fetch_via_archive(project: str, branch: str, scope: Optional[str]) -> Dict[str, Any]:
    """兜底：GitLab archive API（全量后本地筛选）。"""
    try:
        import gitlab  # type: ignore
    except ImportError:
        return {"ok": False, "error": "未安装 python-gitlab"}

    pat = gitlab_pat()
    if not pat:
        return {"ok": False, "error": "取不到 GitLab PAT"}

    host = env.cfg_get("gitlab", "host", default="https://gitlab.gz.cvte.cn")
    verify = env.cfg_get("gitlab", "ssl_verify", default=True)
    gl = gitlab.Gitlab(host, private_token=pat, api_version=4, ssl_verify=verify)
    proj = gl.projects.get(project)
    commit = proj.commits.get(branch)
    sha = commit.id
    sha8 = sha[:8]

    snap = snapshot_dir(project, branch, sha8)
    src = snap / "src"
    if src.exists():
        shutil.rmtree(src, ignore_errors=True)
    src.mkdir(parents=True, exist_ok=True)

    tmp = snap / "_archive.tar.gz"
    with open(tmp, "wb") as f:
        proj.repository_archive(sha=branch, streamed=True, file=f)
    import tarfile
    with tarfile.open(tmp, "r:*") as t:
        t.extractall(src)
    tmp.unlink(missing_ok=True)

    # archive 会套一层 <project>-<sha>/ 前缀，拍平
    children = [p for p in src.iterdir() if p.is_dir()]
    if len(children) == 1 and not any(p.is_file() for p in src.iterdir()):
        inner = children[0]
        for p in inner.iterdir():
            shutil.move(str(p), str(src / p.name))
        inner.rmdir()

    return {"ok": True, "method": "archive", "sha": sha, "sha8": sha8,
            "snapshot": str(snap), "src": str(src), "branch": branch, "project": project}


def ensure_code(project: str, branch: str, scope: Optional[str] = None) -> Dict[str, Any]:
    """取代码：先 git，失败退 archive。"""
    res = fetch_via_git(project, branch, scope)
    if not res.get("ok"):
        env.log(f"  git 路径失败，改用 archive 兜底：{res.get('error','')[:200]}")
        res = fetch_via_archive(project, branch, scope)
    if not res.get("ok"):
        return res

    # 双重保证：快照目录里不该有 .git（物理上无法 push）
    dot_git = Path(res["snapshot"]) / ".git"
    if dot_git.exists():
        shutil.rmtree(dot_git, ignore_errors=True)
    res["has_git_dir"] = (Path(res["snapshot"]) / ".git").exists()
    return res


# ---------------------------------------------------------------- CLAUDE.md


def claude_md_cache_dir(project: str, branch: str) -> Path:
    return env.workspace_root() / "claude_md_cache" / f"{repo_dir_name(project)}@{branch}"


def find_claude_mds(root: Path) -> List[Path]:
    return sorted(p for p in root.rglob("CLAUDE.md") if p.is_file())


def mdmap(args: List[str], cwd: Path, timeout: int = 3600) -> subprocess.CompletedProcess:
    """调 claude-md-map 的 mdmap.py（纯标准库，可用本 venv 跑）。"""
    script = env.cfg_path("paths", "claude_md_map")
    if not script or not script.exists():
        raise FileNotFoundError(f"找不到 mdmap.py: {script}")
    return env.run_python([str(script), *args], cwd=str(cwd), timeout=timeout)


def seed_cache_from_local(seed_root: Path, scope: str, cache: Path) -> int:
    """
    从工具内 docs_seed/ 播种 CLAUDE.md 缓存。

    为什么需要：mdmap.py 的全量 INIT 是**交互式**的 —— 它只跑到
    scan/plan/brief 生成 worker brief，真正的 CLAUDE.md 由 subagent 写 draft 再 install。
    在按需流水线里这需要 Claude 会话介入（可以，但要额外一轮 subagent）。
    若 docs_seed/<repo>@<branch>/ 里已经预放了一整套 CLAUDE.md，直接播种，省掉这条链路。

    注意：这里只**复制** CLAUDE.md 文档本身，代码永远来自工具自己的工作区快照。
    seed 目录在工具内（默认 docs_seed/），**不碰用户本地 clone**。
    """
    scope_dir = seed_root / scope if scope else seed_root
    if not scope_dir.exists():
        scope_dir = seed_root
    found = [p for p in scope_dir.rglob("CLAUDE.md")
             if p.is_file() and ".claude-md-map" not in p.parts]
    if not found:
        return 0
    cache.mkdir(parents=True, exist_ok=True)
    for p in found:
        try:
            rel = p.relative_to(scope_dir)
        except ValueError:
            continue
        dest = cache / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
    return len(found)


def prepare_claude_md(repo: Dict[str, Any]) -> Dict[str, Any]:
    """
    在快照目录里准备 CLAUDE.md。

    流程：
      1. 缓存命中 → 复制进快照 + detect-changes 看有无变更
      2. 缓存未命中，但有本地 clone 的 CLAUDE.md 体系 → 播种缓存（可选，config.local_seed_dir）
      3. 都没有 → 跑 claude-md-map 的 detect/scan/plan/brief 生成 **worker brief**，
         交给 Claude 会话派 subagent 写 draft，再 install（见 CLAUDE_MD_PENDING）

    注意 claude-md-map 的 CLI 是确定性的 scan/plan/brief/install，
    真正的 CLAUDE.md 内容由 subagent 写 —— 所以第 3 步在本 CLI 里只能到 brief 为止。
    """
    snap = Path(repo["snapshot"])
    src = Path(repo["src"])
    project = repo["project"]
    branch = repo["branch"]
    scope_dir = src / repo["scope"] if repo.get("scope") else src
    if not scope_dir.exists():
        scope_dir = src

    cache = claude_md_cache_dir(project, branch)
    existing = find_claude_mds(scope_dir) or find_claude_mds(src)

    result: Dict[str, Any] = {"cache_dir": str(cache), "scope_dir": str(scope_dir)}

    if find_claude_mds(cache) if cache.exists() else False:
        env.log(f"  CLAUDE.md 缓存命中 → 铺进快照，并做增量刷新")
        _copy_claude_mds(cache, scope_dir)
        result["mode"] = "reuse+update"
        try:
            cp = mdmap(["detect"], cwd=scope_dir, timeout=900)
            result["detect"] = (cp.stdout or "").strip()[:500]
            # UPDATE 模式：增量补新模块，不整篇重写
            cp2 = mdmap(["plan"], cwd=scope_dir, timeout=1800)
            result["plan"] = (cp2.stdout or "").strip()[:500]
        except Exception as e:  # noqa: BLE001
            result["update_error"] = str(e)
    else:
        # 2) 尝试用工具内 docs_seed/ 里预放的 CLAUDE.md 播种
        #    注意：seed 目录在**工具内**（config.claude_md.local_seed_dir，默认 docs_seed），
        #    不指向用户本地 clone —— 代码永远来自工具自己的工作区快照。
        seeded = 0
        seed_root = env.tool_path(env.cfg_get("claude_md", "local_seed_dir", default=None))
        if seed_root and seed_root.exists():
            # 首选 docs_seed/<repo>@<branch>/：与 claude_md_cache 同构（已按 scope 剥离），
            # 多个仓库可以并存互不干扰。
            per_repo = seed_root / f"{repo_dir_name(repo['project'])}@{repo['branch']}"
            if per_repo.exists():
                seeded = seed_cache_from_local(per_repo, "", cache)
            else:
                # 兼容：docs_seed/ 下直接按 <scope>/ 组织
                seeded = seed_cache_from_local(seed_root, repo.get("scope") or "", cache)
            if seeded:
                env.log(f"  从 docs_seed 播种了 {seeded} 份 CLAUDE.md 到缓存")
                _copy_claude_mds(cache, scope_dir)

        if seeded:
            result["mode"] = "seeded"
            result["seeded"] = seeded
        else:
            # 3) 跑到 brief 为止，交 Claude 会话派 subagent 写 draft
            env.log(f"  CLAUDE.md 缓存未命中 → 生成 worker brief（需 Claude 派 subagent 写 draft）")
            result["mode"] = "brief-only"
            try:
                cp = mdmap(["detect"], cwd=scope_dir, timeout=900)
                result["detect"] = (cp.stdout or "").strip()[:500]
                cp2 = mdmap(["scan", "--repo", str(scope_dir)], cwd=scope_dir, timeout=1800)
                result["scan"] = (cp2.stdout or "").strip()[-300:]
                scan_json = scope_dir / ".claude-md-map" / "tmp" / "scan.json"
                if scan_json.exists():
                    cp3 = mdmap(["plan", "--scan", str(scan_json)], cwd=scope_dir, timeout=1800)
                    result["plan"] = (cp3.stdout or "").strip()[-300:]
                    modules_json = scope_dir / ".claude-md-map" / "tmp" / "modules.json"
                    if modules_json.exists():
                        cp4 = mdmap(["brief", "--modules", str(modules_json),
                                     "--scan", str(scan_json), "--mode", "init"],
                                    cwd=scope_dir, timeout=1800)
                        result["brief"] = (cp4.stdout or "").strip()[-500:]
                        result["briefs_ready"] = True
            except Exception as e:  # noqa: BLE001
                result["error"] = str(e)

    result["claude_mds"] = [str(p) for p in find_claude_mds(scope_dir)]
    result["root_claude_md"] = (
        str(scope_dir / "CLAUDE.md") if (scope_dir / "CLAUDE.md").exists() else
        (result["claude_mds"][0] if result["claude_mds"] else None)
    )
    env.write_json(snap / "claude_md_status.json", result)
    return result


def _copy_claude_mds(from_dir: Path, to_dir: Path) -> None:
    """把缓存里的 CLAUDE.md 按相对路径复制到目标目录。"""
    for p in find_claude_mds(from_dir):
        rel = p.relative_to(from_dir)
        dest = to_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)


def snapshot_claude_md(repo: Dict[str, Any]) -> None:
    """把快照里生成的 CLAUDE.md 收进缓存（供下次复用）。"""
    cache = claude_md_cache_dir(repo["project"], repo["branch"])
    src = Path(repo["src"])
    scope_dir = src / repo["scope"] if repo.get("scope") else src
    if not scope_dir.exists():
        scope_dir = src
    found = find_claude_mds(scope_dir)
    if not found:
        return
    cache.mkdir(parents=True, exist_ok=True)
    for p in found:
        rel = p.relative_to(scope_dir)
        dest = cache / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(p, dest)
    env.write_json(cache / ".meta.json", {
        "project": repo["project"], "branch": repo["branch"],
        "sha": repo.get("sha"), "files": [str(p.relative_to(cache)) for p in
                                          (cache.rglob("CLAUDE.md"))],
    })
    env.log(f"  CLAUDE.md 已存入缓存 {cache.name}")


if __name__ == "__main__":
    import argparse
    import json as _json

    ap = argparse.ArgumentParser(description="取代码到工具自己的工作区")
    ap.add_argument("--project", required=True, help="GitLab 项目路径，如 group/sub/repo")
    ap.add_argument("--branch", required=True)
    ap.add_argument("--scope", help="只取这个子目录")
    a = ap.parse_args()
    out = ensure_code(a.project, a.branch, a.scope)
    print(_json.dumps(out, ensure_ascii=False, indent=2))
