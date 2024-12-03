#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = CWD.split('/')[-1]
YEAR = CWD.split('/')[-2]

logger = logging.getLogger(f"{YEAR}:d{DAY}")


def parse_file(filename):
    pass


def part_one(my_input):
    pass


def part_two(my_input):
    pass


if __name__ == "__main__":
    logger.info("")
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 123
    assert part_two(my_input) == 123

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 123
    assert part_two(my_input) == 123
