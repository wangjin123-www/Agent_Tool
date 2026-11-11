#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HC32 DAB编译摘要生成器
解析Keil编译日志，生成txt格式编译报告
"""

import sys
import re
import os
from pathlib import Path
from datetime import datetime
import subprocess

def parse_build_log(log_file):
    """解析编译日志"""
    if not os.path.exists(log_file):
        return {
            'success': False,
            'errors': ['编译日志不存在'],
            'warnings': [],
            'error_count': 1,
            'warning_count': 0,
            'compile_time': 0,
            'compiler': 'Unknown',
            'target': 'Unknown',
            'config': 'Unknown'
        }

    with open(log_file, 'r', encoding='utf-8', errors='ignore') as f:
        log_content = f.read()

    # 提取编译器信息
    compiler_match = re.search(r"Compiler '(V\d+\.\d+[^\']*)'", log_content)
    compiler = compiler_match.group(1) if compiler_match else 'Unknown'

    # 提取目标和配置
    target_match = re.search(r"Build target '([^']+)'", log_content)
    target = target_match.group(1) if target_match else 'Unknown'

    # 统计错误和警告 - 从最终结果行提取
    errors = []
    warnings = []
    result_match = re.search(r'"([^"]+)" - (\d+) Error\(s\), (\d+) Warning\(s\)', log_content)
    if result_match:
        error_count = int(result_match.group(2))
        warning_count = int(result_match.group(3))
    else:
        # 备用方案：逐行统计
        errors = re.findall(r'.+\d+\s+Error\s+\d+.+', log_content, re.IGNORECASE)
        warnings = re.findall(r'.+\d+\s+Warning\s+\d+.+', log_content, re.IGNORECASE)
        error_count = len(errors)
        warning_count = len(warnings)

    # 判断编译是否成功
    success = error_count == 0

    # 提取编译时间 (格式: 00:00:13)
    time_match = re.search(r'Build Time Elapsed:\s+(\d+):(\d+):(\d+)', log_content)
    if time_match:
        compile_time = int(time_match.group(1)) * 3600 + int(time_match.group(2)) * 60 + int(time_match.group(3))
    else:
        compile_time = 0

    # 确定配置
    config = 'Debug' if 'debug' in log_content.lower() else 'Release'

    return {
        'success': success,
        'errors': errors[:10],
        'warnings': warnings[:10],
        'error_count': error_count,
        'warning_count': warning_count,
        'compile_time': compile_time,
        'compiler': compiler,
        'target': target,
        'config': config,
        'log_content': log_content
    }

def get_file_sizes(output_dir):
    """获取输出文件大小"""
    files = {}
    output_path = Path(output_dir).resolve()

    # 查找AXF文件
    axf_files = list(output_path.glob('**/*.axf'))
    if axf_files:
        axf_size = axf_files[0].stat().st_size / (1024 * 1024)
        files['axf'] = f"{axf_size:.1f} MB"
        files['axf_path'] = str(axf_files[0])

    # 查找HEX文件
    hex_files = list(output_path.glob('**/*.hex'))
    if hex_files:
        hex_size = hex_files[0].stat().st_size / 1024
        files['hex'] = f"{hex_size:.0f} KB"
        files['hex_path'] = str(hex_files[0])

    # 查找BIN文件
    bin_files = list(output_path.glob('**/*.bin'))
    if bin_files:
        bin_size = bin_files[0].stat().st_size / 1024
        files['bin'] = f"{bin_size:.0f} KB"
        files['bin_bytes'] = bin_files[0].stat().st_size
        files['bin_path'] = str(bin_files[0])

    return files

def parse_memory_usage(log_content):
    """解析内存使用情况"""
    memory_info = {}

    # 查找Code段大小
    code_match = re.search(r'Code=(\d+)', log_content)
    if code_match:
        memory_info['code'] = int(code_match.group(1))

    # 查找RO-data大小
    ro_match = re.search(r'RO-data=(\d+)', log_content)
    if ro_match:
        memory_info['ro'] = int(ro_match.group(1))

    # 查找RW-data大小
    rw_match = re.search(r'RW-data=(\d+)', log_content)
    if rw_match:
        memory_info['rw'] = int(rw_match.group(1))

    # 查找ZI-data大小
    zi_match = re.search(r'ZI-data=(\d+)', log_content)
    if zi_match:
        memory_info['zi'] = int(zi_match.group(1))

    # 查找Debug大小
    debug_match = re.search(r'Debug\s+(\d+)', log_content)
    if debug_match:
        memory_info['debug'] = int(debug_match.group(1))

    return memory_info

def generate_summary(build_log, output_dir, project_name='HC32F460PETB DAB盒子'):
    """生成编译摘要"""
    # 解析编译日志
    build_info = parse_build_log(build_log)

    # 获取文件大小
    file_info = get_file_sizes(output_dir)

    # 解析内存使用
    memory_info = parse_memory_usage(build_info.get('log_content', ''))

    # 计算总大小（字节转KB）
    total_flash_bytes = memory_info.get('code', 0) + memory_info.get('ro', 0)
    total_ram_bytes = memory_info.get('rw', 0) + memory_info.get('zi', 0)
    total_flash_kb = total_flash_bytes / 1024
    total_ram_kb = total_ram_bytes / 1024

    # Flash总容量（HC32F460PETB: 256KB Flash）
    flash_capacity_kb = 256

    # 生成报告
    report = f"""=== 编译调试报告 ===
时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
工程: {project_name}

【编译结果】
状态: {'成功' if build_info['success'] else '失败'}
错误数: {build_info['error_count']}
警告数: {build_info['warning_count']}
编译时间: {build_info['compile_time']}秒

【输出文件】
AXF文件: {file_info.get('axf', 'N/A')} (含调试符号)
  路径: {file_info.get('axf_path', 'N/A')}
HEX文件: {file_info.get('hex', 'N/A')} (Intel HEX格式)
  路径: {file_info.get('hex_path', 'N/A')}
BIN文件: {file_info.get('bin', 'N/A')} (纯二进制固件)
  路径: {file_info.get('bin_path', 'N/A')}

【固件大小分析】
实际代码: {file_info.get('bin', 'N/A')}
Flash占用: {total_flash_kb:.1f} KB / {flash_capacity_kb} KB ({total_flash_kb/flash_capacity_kb*100:.1f}%)
RAM占用: {total_ram_kb:.1f} KB

【内存详情】
Code: {memory_info.get('code', 0)} 字节
RO-data: {memory_info.get('ro', 0)} 字节
RW-data: {memory_info.get('rw', 0)} 字节
ZI-data: {memory_info.get('zi', 0)} 字节

【编译信息】
编译器: ARM Compiler {build_info['compiler']}
目标: {build_info['target']}
配置: {build_info['config']}

【结论】
{'编译成功，固件已生成' if build_info['success'] else f'编译失败，存在 {build_info["error_count"]} 个错误'}
"""

    return report

def generate_bin_file(axf_file, output_bin):
    """调用 fromelf.exe 生成 bin 文件"""
    fromelf_path = r"D:\\keil\\ARM\\ARMCLANG\\bin\\fromelf.exe"
    try:
        subprocess.run([fromelf_path, "--bin", f"--output={output_bin}", axf_file], check=True)
        print(f"成功生成 bin 文件: {output_bin}")
    except subprocess.CalledProcessError as e:
        print(f"生成 bin 文件失败: {e}")

def main():
    if len(sys.argv) < 3:
        print("用法: python generate_build_summary.py <build_log> <output_dir> [project_name]")
        print("示例: python generate_build_summary.py MDK/build.log MDK/output/debug")
        sys.exit(1)

    build_log = sys.argv[1]
    output_dir = sys.argv[2]
    project_name = sys.argv[3] if len(sys.argv) > 3 else 'HC32F460PETB DAB盒子'

    # 生成摘要
    summary = generate_summary(build_log, output_dir, project_name)

    # 确定输出文件路径（相对于脚本所在目录）
    script_dir = Path(__file__).parent.parent
    output_file = script_dir / 'output' / 'build_summary.txt'

    # 写入文件
    output_file.parent.mkdir(parents=True, exist_ok=True)
    output_file.write_text(summary, encoding='utf-8')

    # Windows兼容输出（避免emoji编码问题）
    try:
        print(f"[OK] Build summary generated: {output_file}")
    except:
        print("[OK] Build summary:", str(output_file))

if __name__ == '__main__':
    main()
