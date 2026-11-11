#!/usr/bin/env python3
"""导出Cortex-M异常状态（寄存器+关键内存），格式化输出"""
import argparse, subprocess, sys, tempfile, os, re

CORTEX_REGS = {
    'CFSR':  '0xE000ED28',
    'HFSR':  '0xE000ED2C',
    'MMFAR': '0xE000ED34',
    'BFAR':  '0xE000ED38',
    'SHCSR': '0xE000ED24',
}

STACK_REGS = {
    'MSP':  '0xE000ED08',  # 直接从向量表读
    'PSP':  '0xE000ED09',
}

def parse_reg_output(text):
    """解析JLink寄存器输出"""
    result = {}
    for line in text.split('\n'):
        m = re.match(r'\s*(\w+)\s*=\s*(0x[0-9A-Fa-f]+)', line)
        if m:
            result[m.group(1)] = m.group(2)
    return result

def parse_mem32_output(text):
    """解析mem32输出"""
    result = {}
    for line in text.split('\n'):
        m = re.match(r'\s*(0x[0-9A-Fa-f]+)\s*=\s*(0x[0-9A-Fa-f]+)', line)
        if m:
            result[m.group(1).upper()] = m.group(2)
    return result

def analyze_fault(cfsr_val, hfsr_val):
    """分析异常原因"""
    reasons = []
    cfsr = int(cfsr_val, 16) if cfsr_val else 0
    hfsr = int(hfsr_val, 16) if hfsr_val else 0

    if cfsr & 0x01: reasons.append('IACCVIOL: 指令访问违规')
    if cfsr & 0x02: reasons.append('DACCVIOL: 数据访问违规')
    if cfsr & 0x08: reasons.append('MUNSTKERR: 出栈错误')
    if cfsr & 0x10: reasons.append('MSTKERR: 入栈错误')
    if cfsr & 0x20: reasons.append('MLSPERR: 浮点惰性状态错误')
    if cfsr & 0x100: reasons.append('IBUSERR: 指令总线错误')
    if cfsr & 0x200: reasons.append('PRECISERR: 精确数据总线错误')
    if cfsr & 0x400: reasons.append('IMPRECISERR: 不精确数据总线错误')
    if cfsr & 0x800: reasons.append('UNSTKERR: 总线出栈错误')
    if cfsr & 0x1000: reasons.append('STKERR: 总线入栈错误')
    if cfsr & 0x2000: reasons.append('LSPERR: 总线浮点惰性错误')
    if cfsr & 0x10000: reasons.append('UNDEFINSTR: 未定义指令')
    if cfsr & 0x20000: reasons.append('INVSTATE: 无效状态(Thumb位)')
    if cfsr & 0x40000: reasons.append('INVPC: 无效PC加载')
    if cfsr & 0x80000: reasons.append('NOCP: 无协处理器')
    if hfsr & 0x00000002: reasons.append('VECTTBL: 向量表读取失败')
    if hfsr & 0x40000000: reasons.append('FORCED: 强制HardFault( escalate)')
    if hfsr & 0x80000000: reasons.append('DEBUGEVT: 调试事件')
    return reasons

def main():
    p = argparse.ArgumentParser()
    p.add_argument('--jlink', required=True)
    p.add_argument('--device', required=True)
    args = p.parse_args()

    mem_addrs = ' '.join(f'mem32 {addr} 1' for addr in CORTEX_REGS.values())
    script = f'connect\nh\nregs\n{mem_addrs}\nq'

    with tempfile.NamedTemporaryFile(mode='w', suffix='.jlink', delete=False, encoding='utf-8') as f:
        f.write(script)
        tmp = f.name

    try:
        result = subprocess.run(
            [args.jlink, '-device', args.device, '-if', 'SWD', '-speed', '4000', '-CommanderScript', tmp],
            capture_output=True, text=True, timeout=30
        )
    finally:
        os.unlink(tmp)

    output = result.stdout
    regs = parse_reg_output(output)
    mems = parse_mem32_output(output)

    addr_map = {v.upper(): k for k, v in CORTEX_REGS.items()}
    fault_regs = {}
    for addr, val in mems.items():
        name = addr_map.get(addr, addr)
        fault_regs[name] = val

    print('=== Cortex-M 异常状态 ===')
    print(f'\n--- 核心寄存器 ---')
    for name in ['PC', 'LR', 'SP', 'PSR', 'R0', 'R1', 'R2', 'R3', 'R12']:
        if name in regs:
            print(f'  {name:6s} = {regs[name]}')

    print(f'\n--- 异常寄存器 ---')
    for name, val in fault_regs.items():
        print(f'  {name:6s} = {val}')

    cfsr = fault_regs.get('CFSR', '0x00000000')
    hfsr = fault_regs.get('HFSR', '0x00000000')
    reasons = analyze_fault(cfsr, hfsr)

    if reasons:
        print(f'\n--- 异常分析 ---')
        for r in reasons:
            print(f'  * {r}')
    else:
        print(f'\n--- 无异常 ---')

if __name__ == '__main__':
    main()
