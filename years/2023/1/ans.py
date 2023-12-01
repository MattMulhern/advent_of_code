#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    chunks = []
    with open(filename, "r") as fp:
        chunks = fp.read().strip().split("\n")
        return chunks


def part_one(my_input):
    logger = logging.getLogger("2022:d1:p1")
    stripped = []
    for line in my_input:
        stripped.append([x for x in line if x.isdigit()])

    total = 0
    for line in stripped:
        total += int(f"{line[0]}{line[-1]}")
    logger.info(f"2022:d1:p1: {total}")
    return total


def part_two(my_input):
    numer_words = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    logger = logging.getLogger("2022:d1:p2")
    converted = []
    total = 0
    for line in my_input:
        before = line
        for word in numer_words:
            line = line.replace(word, str(f"{word}{numer_words.index(word)}{word}"))
        converted.append(line)
        values = [x for x in line if x.isdigit()]
        value = int(f"{values[0]}{values[-1]}")
        logger.info(f"{before} -> {line} -> {value}")
        total += value
    logger.info(f"2022:d1:p2: {total}")
    return total


if __name__ == "__main__":
    ex_1_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(ex_1_input) == 142

    ex_2_input = parse_file(os.path.join(CWD, "example2.txt"))
    assert part_two(ex_2_input) == 281

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 55834
    assert part_two(my_input) == 53221
