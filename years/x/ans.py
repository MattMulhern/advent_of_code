#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    chunks = []
    with open(filename, "r") as fp:
        chunks = fp.read().split("\n\n")
        return chunks


def part_one(my_input):
    logger = logging.getLogger("2022:dX:p1")


def part_two(my_input):
    logger = logging.getLogger("2022:dX:p2")


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 123
    assert part_two(my_input) == 123

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 123
    assert part_two(my_input) == 123
