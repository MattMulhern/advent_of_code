#!/usr/bin/env python3
import logging
import os
from collections import Counter

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    with open(filename, "r") as fp:
        return fp.read().strip()


def find_marker(logger, buffer, num_uniq_chars=4):
    width = num_uniq_chars - 1
    for idx, val in enumerate(buffer):
        if idx < (width):
            continue
        substr = buffer[idx - width : idx + 1]
        counter = Counter(substr)
        if counter.most_common()[0][1] == 1:
            letter = idx + 1
            logger.info(
                f"found {num_uniq_chars} unique characters [{substr}] at letter {letter}"
            )
            return letter


def part_one(buffer):
    logger = logging.getLogger("2022:d6:p1")
    return find_marker(logger, buffer, num_uniq_chars=4)


def part_two(buffer):
    logger = logging.getLogger("2022:d6:p2")
    return find_marker(logger, buffer, num_uniq_chars=14)


if __name__ == "__main__":
    assert part_one("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 7
    assert part_one("bvwbjplbgvbhsrlpgdmjqwftvncz") == 5
    assert part_one("nppdvjthqldpwncqszvftbrmjlhg") == 6
    assert part_one("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 10
    assert part_one("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 11

    assert part_two("mjqjpqmgbljsphdztnvjfqwrcgsmlb") == 19
    assert part_two("bvwbjplbgvbhsrlpgdmjqwftvncz") == 23
    assert part_two("nppdvjthqldpwncqszvftbrmjlhg") == 23
    assert part_two("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg") == 29
    assert part_two("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw") == 26

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 1623
    assert part_two(my_input) == 3774
