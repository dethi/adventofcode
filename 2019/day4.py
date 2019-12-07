#!/usr/bin/env python3

import sys

from collections import Counter


def get_digits(n):
    return [int(d) for d in str(n)]


def check_increase(digits):
    for i in range(0, len(digits)-1):
        if digits[i] > digits[i+1]:
            return False
    return True


def check_adjacent(digits):
    for i in range(0, len(digits)-1):
        if digits[i] == digits[i+1]:
            return True
    return False


def check_double(digits):
    return any(cnt == 2 for cnt in Counter(digits).values())


def main(low, high):
    acc = 0
    for n in range(low, high+1):
        digits = get_digits(n)

        predicats = (
            check_increase,
            check_adjacent,
            check_double
        )
        if all(map(lambda fn: fn(digits), predicats)):
            acc += 1

    print(f'acc={acc}')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage: ./script.py [low] [high]')
        sys.exit(1)

    main(int(sys.argv[1]), int(sys.argv[2]))
