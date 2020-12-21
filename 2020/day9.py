#!/usr/bin/env python3

import sys


def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    nums = list(map(int, lines))

    preamble_size = 25
    preamble = set(nums[:preamble_size - 1])
    for i in range(preamble_size, len(nums)):
        preamble.add(nums[i - 1])
        for n in preamble:
            if nums[i] - n in preamble:
                break
        else:
            print(f'part 1: {nums[i]=}')
            break

        preamble.remove(nums[i - preamble_size])

    target = nums[i]
    for i in range(len(nums) - 1):
        acc = nums[i]

        for j in range(i+1, len(nums)):
            acc += nums[j]
            if acc == target:
                arr = nums[i:j + 1]
                weakness = min(arr) + max(arr)
                print(f'part 2: {weakness=}')
                return

            if acc > target:
                break
    else:
        print('no solution found')


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
