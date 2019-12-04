#!/usr/bin/env python3

import sys
import operator

from functools import reduce
from typing import List, Tuple, Iterator


Vector = Tuple[int, int] # x, y


def decode_move(move: str) -> Vector:
    d, n = move[0], int(move[1:])
    if d == 'U':
        return (0, n)
    elif d == 'D':
        return (0, -n)
    elif d == 'L':
        return (-n, 0)
    elif d == 'R':
        return (n, 0)
    else:
        raise ValueError(f"invalid direction d={d}")


def decode_path(path: str) -> List[Vector]:
    return [decode_move(move) for move in path.split(',')]


def unit_vect(move: Vector) -> Iterator[Vector]:
    x, y = move
    if x != 0:
        return ((int(x/abs(x)), 0) for _ in range(abs(x)))
    else:
        return ((0, int(y/abs(y))) for _ in range(abs(y)))


def vect_add(v1: Vector, v2: Vector) -> Vector:
    return tuple(map(operator.add, v1, v2))


def dist(v1: Vector, v2: Vector) -> int:
    return abs(v1[0] - v2[0]) + abs(v1[1] - v2[1])


def main(input_file: str):
    with open(input_file) as f:
        lines = f.readlines()

    wires = [decode_path(line) for line in lines]
    grids = [{} for _ in wires]
    origin = (0, 0)

    for i, wire in enumerate(wires):
        pos = origin
        d = 0

        for move in wire:
            for vu in unit_vect(move):
                pos = vect_add(pos, vu)
                d += 1

                grids[i].setdefault(pos, d)

    intersections = reduce(set.intersection, map(set, grids))

    minD = float('inf')
    minSteps = float('inf')
    for pos in intersections:
        minD = min(minD, dist(origin, pos))
        minSteps = min(minSteps, sum(g[pos] for g in grids))

    print(f'Min distance = {minD}')
    print(f'Min steps = {minSteps}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py <input-file>')
        sys.exit(1)

    main(sys.argv[1])
