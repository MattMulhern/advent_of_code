#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    pairs = []
    with open(filename, "r") as fp:
        for line in fp.readlines():
            left, right = line.strip().split(',')
            left_ranges = [int(x) for x in left.split('-')]
            left_sections = list(range(left_ranges[0],left_ranges[1]+1))
            right_ranges = [int(x) for x in right.split('-')]
            right_sections = list(range(right_ranges[0], right_ranges[1]+1))
            pairs.append((left_sections, right_sections))
    return pairs


def part_one(pairs):
    logger = logging.getLogger("2022:d4:p1")
    total_subsets = 0
    for pair in pairs:
        if (set(pair[0]).issubset(set(pair[1]))) or (set(pair[1]).issubset(set(pair[0]))):
            # logger.debug(f"found subset: {pair}")
            total_subsets += 1
    logger.info(f"found {total_subsets} overlapping shifts")
    return total_subsets


def part_two(pairs):
    logger = logging.getLogger("2022:d4:p2")
    total_overlaps = 0
    for pair in pairs:
        overlaps = set(pair[0]).intersection(pair[1])
        if len(overlaps) > 0:
            # logger.debug(f"found overlap: [{overlaps}] for pair {pair}")
            total_overlaps += 1
    logger.info(f"found {total_overlaps} overlapping shifts")
    return total_overlaps



if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 2
    assert part_two(my_input) == 4

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 534
    assert part_two(my_input) == 841
