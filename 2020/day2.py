#!/usr/bin/env python3

import re
import sys


line_re = re.compile(r'(?P<low>\d+)-(?P<upper>\d+) (?P<char>\w): (?P<passwd>.*)')


def parse_line(line):
    m = line_re.match(line)
    return m.groupdict()


def is_valid_1(low=0, upper=0, char='', passwd=''):
    low, upper = int(low), int(upper)
    return low <= passwd.count(char) <= upper


def is_valid_2(low=0, upper=0, char='', passwd=''):
    low, upper = int(low), int(upper)
    return sum(map(lambda i: passwd[i - 1] == char, (low, upper))) == 1


def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    n_valid_1 = sum(is_valid_1(**parse_line(line)) for line in lines)
    n_valid_2 = sum(is_valid_2(**parse_line(line)) for line in lines)
    print(f'{n_valid_1=} {n_valid_2=}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
