#!/usr/bin/env python3

import sys


def main(input_file):
    with open(input_file) as f:
        buf = f.read()

    groups = buf.split('\n\n')
    count_anyone = sum(len(set(group.replace('\n', ''))) for group in groups)
    print(f'{count_anyone=}')

    count_everyone = sum(
        len(set.intersection(*map(set, group.strip().split('\n'))))
        for group in groups
    )
    print(f'{count_everyone=}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
