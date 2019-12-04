#!/usr/bin/env python3

import sys
from functools import lru_cache

@lru_cache(maxsize=None)
def compute_fuel(mass):
    fuel = mass // 3 - 2
    if fuel > 0:
        return fuel + compute_fuel(fuel)
    return 0

def main(input_file):
    with open(input_file)as f:
        res = sum(compute_fuel(int(line)) for line in f.readlines())
        print(res)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
