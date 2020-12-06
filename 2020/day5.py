#!/usr/bin/env python3

import sys

from itertools import islice, chain


def search(barcode, lo, hi):
    if lo == hi:
        return lo

    c = barcode[0]
    if c == 'F' or c == 'L':
        hi = (lo + hi) // 2
    else:
        lo = (lo + hi) // 2 + 1

    return search(barcode[1:], lo, hi)


def convert(barcode):
    row = search(barcode[:7], 0, 127)
    col = search(barcode[7:], 0, 7)
    return row, col


def seat_id(row, col):
    return row * 8 + col


def window(seq, n=2):
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result


def missing_elements(L, count):
    missing = chain.from_iterable(range(x + 1, y) for x, y in window(L) if (y - x) > 1)
    return list(islice(missing, 0, count))


def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    max_seat_id = max(seat_id(*convert(barcode)) for barcode in lines)
    print(f'{max_seat_id=}')

    seat_ids = sorted([seat_id(*convert(barcode)) for barcode in lines])
    missing_seat_id = missing_elements(seat_ids, 1)
    print(f'{missing_seat_id=}')



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
