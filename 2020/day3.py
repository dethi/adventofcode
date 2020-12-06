#!/usr/bin/env python3

import sys


def gen_move(mr, md, height):
    right, down = 0, 0
    for _ in range(height//md):
        right += mr
        down += md
        yield (right, down)


def get(grid, right, down):
    line = grid[down]
    return line[right % (len(line) - 1)]


def main(input_file):
    with open(input_file) as f:
        grid = f.readlines()

    h = len(grid) - 1
    steps = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    total = 1

    for (mr, md) in steps:
        g = gen_move(mr, md, h)
        trees = sum(get(grid, right, down) == '#' for (right, down) in g)
        print(f'right={mr} down={md} {trees=}')

        total *= trees

    print(f'{total=}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
