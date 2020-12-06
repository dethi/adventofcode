#!/usr/bin/env python3

import re
import sys


required_fields = (
    re.compile(r'byr:(19[2-9][0-9]|200[0-2])(\s|$)'),
    re.compile(r'iyr:(201[0-9]|2020)(\s|$)'),
    re.compile(r'eyr:(202[0-9]|2030)(\s|$)'),
    re.compile(r'hgt:((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)(\s|$)'),
    re.compile(r'hcl:#[0-9a-f]{6}(\s|$)'),
    re.compile(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)(\s|$)'),
    re.compile(r'pid:[0-9]{9}(\s|$)')
)


def validate_passport(passport):
    for field in required_fields:
        if field.search(passport) is None:
            return False
    return True


def main(input_file):
    with open(input_file) as f:
        buf = f.read()

    valid = sum(validate_passport(p) for p in buf.split('\n\n'))
    print(f'{valid=}')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
