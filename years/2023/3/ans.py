#!/usr/bin/env python3
import logging
import os
import numpy as np

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    with open(filename, "r") as fp:
        return [list(line.strip()) for line in fp.readlines()]


def part_one(engine):
    logger = logging.getLogger("2023:d3:p1")
    not_symbols = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]

    # create an map of all valid engine part spots on the schematic
    width = len(engine)
    height = len(engine[0])
    map = np.zeros((width, height), dtype=bool)

    # list of diffs to iterate over the surrounding cells
    diffs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    for i in range(width):
        for j in range(height):
            if engine[i][j] not in not_symbols:
                for di, dj in diffs:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < width and 0 <= nj < height:
                        map[ni][nj] = True

    output = 0
    tmp_num = ""
    tmp_valid = False
    for i in range(0, width):
        for j in range(0, height):
            if engine[i][j] in not_symbols and engine[i][j] != ".":
                tmp_num = tmp_num + engine[i][j]
                tmp_valid = map[i][j] or tmp_valid
            else:
                if tmp_num != "" and tmp_valid:
                    output = output + int(tmp_num)
                tmp_num = ""
                tmp_valid = False
        if tmp_num != "" and tmp_valid:
            output = output + int(tmp_num)
        tmp_num = ""
        tmp_valid = False
    logger.info(output)
    return output


def part_two(my_input):
    logger = logging.getLogger("2023:d3:p2")


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 4361
    # assert part_two(my_input) == 123

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 533784
    # assert part_two(my_input) == 123
