#!/usr/bin/env python3
import logging
import os
import string

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    bags = []
    with open(filename, "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        for line in lines:
            bags.append((line[: int(len(line) / 2)], line[int(len(line) / 2) :]))
    return bags


def chunk_file(filename):
    chunked = []
    chunk_size = 3
    with open(filename, "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        for i in range(0, len(lines), chunk_size):
            chunked.append(lines[i : i + chunk_size])
    return chunked


def get_priority(item):
    return string.ascii_letters.index(item) + 1


def part_one(my_input):
    logger = logging.getLogger("2022:d3:p1")
    total_priorities = 0
    for bag in my_input:
        common = set(bag[0]).intersection(bag[1])
        assert len(common) == 1
        common_item = str(list(common)[0])
        item_priority = get_priority(common_item)
        # logger.debug(f"common item in {bag} is {common_item} which scores {item_priority}")
        total_priorities += item_priority
    logger.info(f"total priorities for bags is {total_priorities}")
    return total_priorities


def part_two(my_input):
    logger = logging.getLogger("2022:dX:p2")
    total_priorities = 0
    for group in my_input:
        common = list(set(group[0]).intersection(group[1]).intersection(group[2]))
        assert len(common) == 1
        common_priority = get_priority(common[0])
        logger.debug(f"common item in {group} is {common} which scores {common_priority}")
        total_priorities += common_priority
    logger.info(f"total priorities for all groups is {total_priorities}")
    return total_priorities


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 157
    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 7817

    my_input = chunk_file(os.path.join(CWD, "example.txt"))
    assert part_two(my_input) == 70
    my_input = chunk_file(os.path.join(CWD, "input.txt"))
    assert part_two(my_input) == 2444
