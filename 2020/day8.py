#!/usr/bin/env python3

import re
import sys


instruction_re = re.compile(r'(?P<op>\w+) (?P<arg>[-+\d]+)')


def parse_line(line):
    m = instruction_re.match(line)
    return m.group('op'), int(m.group('arg'))


def run(prog):
    pc = 0
    mem = 0
    while pc < len(prog) and prog[pc]:
        op, arg = prog[pc]
        prog[pc] = None # erase intruction

        if op == 'nop':
            pc += 1
        elif op == 'acc':
            mem += arg
            pc += 1
        elif op == 'jmp':
            pc += arg
        else:
            raise RuntimeError(f'invalid instruction: {op=} {arg=}')

    # (True, mem) or (False, mem) if infinite loop found
    return pc == len(prog), mem


def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    prog = list(map(parse_line, lines))

    _, mem = run(prog.copy())
    print(f'part 1: {mem=}')

    # part 2
    for i in range(len(prog)):
        op, arg = prog[i]
        if op == 'nop':
            op = 'jmp'
        elif op == 'jmp':
            op = 'nop'
        else:
            continue # skip run if no instruction swap

        forked_prog = prog.copy()
        forked_prog[i] = (op, arg)
        ok, mem = run(forked_prog)
        if ok:
            print(f'part 2: {mem=}')
            break


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
