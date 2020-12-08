#!/usr/bin/env python3

import re
import sys

from collections import defaultdict, deque


contain_re = re.compile(r'(?P<count>\d+) (?P<name>[a-z ]+) bags?')


def parse_line(line):
    bag, contained = line.split(' bags contain ')
    contained = [
        (int(m.group('count')), m.group('name'))
        for m in contain_re.finditer(contained)
    ]
    return bag, contained


def part_1(lines):
    graph = defaultdict(set)
    for bag, contained in map(parse_line, lines):
        for _, b in contained:
            graph[b].add(bag)

    q = deque(['shiny gold'])
    visited = set(['shiny gold'])

    while q:
        bag = q.popleft()
        for b in graph.get(bag, []):
            if b not in visited:
                q.append(b)
                visited.add(b)

    count = len(visited) - 1
    print(f'part1 {count=}')


def count_bags(graph, bag):
    if bag not in graph:
        return 0
    return 1 + sum(n * count_bags(graph, b) for n, b in graph[bag])


def part_2(lines):
    graph = {bag: contained for bag, contained in map(parse_line, lines)}
    count = count_bags(graph, "shiny gold") - 1
    print(f'part2: {count=}')


def main(input_file):
    with open(input_file) as f:
        lines = f.readlines()

    part_1(lines)
    part_2(lines)


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage: ./script.py [input-file]')
        sys.exit(1)

    main(sys.argv[1])
