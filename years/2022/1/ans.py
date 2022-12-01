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


def part_one(chunks):
    logger = logging.getLogger("2022:d1:p1")
    highest_calories = 0
    elf_idx_with_most = None
    for idx, elf in enumerate(chunks, 1):  # the question starts counting elves at 1
        total_calories = sum([int(x) for x in elf.split("\n")])
        if total_calories > highest_calories:
            highest_calories = total_calories
            elf_idx_with_most = idx
    logger.info(
        f"Elf no. {elf_idx_with_most} had the most calories [{highest_calories}]"
    )
    return elf_idx_with_most, highest_calories  # add 1 since indexing starts at


def part_two(chunks):
    logger = logging.getLogger("2022:d1:p2")
    elves_by_calories = {}
    for idx, elf in enumerate(chunks, 1):  # the question starts counting elves at 1
        total_calories = sum([int(x) for x in elf.split("\n")])
        if total_calories in elves_by_calories.keys():
            raise ValueError("Two elves with the same total calories??")
        else:
            elves_by_calories[total_calories] = idx
    cal_list = sorted(elves_by_calories.keys(), reverse=True)
    total_of_top_3 = cal_list[0] + cal_list[1] + cal_list[2]
    logger.debug(
        f"The top three are:"
        f"{elves_by_calories[cal_list[0]]} with {cal_list[0]}, "
        f"{elves_by_calories[cal_list[1]]} with {cal_list[1]} and "
        f"{elves_by_calories[cal_list[2]]} with {cal_list[2]}, "
        f"making a total of {total_of_top_3}"
    )
    return total_of_top_3


if __name__ == "__main__":
    chunks = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(chunks)[0] == 4
    assert part_two(chunks) == 45000

    chunks = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(chunks)[1] == 68467
    assert part_two(chunks) == 203420
