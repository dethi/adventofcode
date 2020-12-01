#!/usr/bin/env python3

import sys
from math import prod
from itertools import combinations


def main(input_file, r):
    with open(input_file) as f:
        num = [int(line) for line in f.readlines()]

    for tup in combinations(num, r):
        if sum(tup) == 2020:
            print(f'{tup=} {prod(tup)}')
            break

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: ./script.py [input-file] [r]')
        sys.exit(1)

    main(sys.argv[1], int(sys.argv[2]))
