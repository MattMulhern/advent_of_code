#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = os.path.basename(CWD)

logger = logging.getLogger(f"2024:d{DAY}")


def parse_file(filename):
    left = []
    right = []
    with open(filename, "r") as fp:
        for line in fp.readlines():
            splitline = line.strip().split()
            left.append(int(splitline[0]))
            right.append(int(splitline[1]))
    return (left, right)


def part_one(my_input):
    left, right = my_input
    left = sorted(left)
    right = sorted(right)
    total_diff = 0
    for nums in zip(left, right):
        diff = abs(nums[0] - nums[1])
        total_diff += diff
    logger.info(f"total_diff: {total_diff}")
    return total_diff


def part_two(my_input):
    left, right = my_input
    total_scores = 0
    for num in left:
        score = (num * right.count(num))
        total_scores += score
    logger.info(f"total_scores: {total_scores}")
    return total_scores


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 11
    assert part_two(my_input) == 31

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 1197984
    assert part_two(my_input) == 23387399
