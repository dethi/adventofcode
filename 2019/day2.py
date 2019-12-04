#!/usr/bin/env python3

import json
import sys

from itertools import chain


def run_prog(prog):
    reg = {i: n for i, n in enumerate(prog)}

    i = 0
    while True:
        opcode = reg[i]
        if opcode == 1:
            arg0 = reg[i+1]
            arg1 = reg[i+2]
            res0 = reg[i+3]

            reg[res0] = reg[arg0] + reg[arg1]
        elif opcode == 2:
            arg0 = reg[i+1]
            arg1 = reg[i+2]
            res0 = reg[i+3]

            reg[res0] = reg[arg0] * reg[arg1]
        elif opcode == 99:
            break
        else:
            print('unknown opcode {}'.format(opcode))
            return

        i += 4

    return reg[0]


def main(input_file, want_ret):
    with open(input_file) as f:
        content = f.read()

    prog = [int(n) for n in content.split(',')]

    for noun in range(100):
        for verb in range(100):
            prog[1] = noun
            prog[2] = verb

            ret = run_prog(prog)
            if ret == want_ret:
                print("noun={}, verb={}".format(noun, verb))
                print("answer={}".format(100 * noun + verb))
                return


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: script.py [input-file] [output]')
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
