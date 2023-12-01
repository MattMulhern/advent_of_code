#!/usr/bin/env python3
import logging
import os
import numpy as np
logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    with open(filename, "r") as fp:
        return [tuple(x.strip().split()) for x in fp.readlines()]


def walk(grid, instruction, hpos, tpos):
    for x in range(instruction[1]):
        grid, hpos, tpos = step(grid, instruction[0], hpos, tpos)
    return grid, hpos, tpos

def step(grid, direction, hpos, tpos):
    if direction == 'U':
        new_xpos = (xpos[0]+1, xpos[1])
    elif direction == 'D':
        new_xpos = (xpos[0]-1, xpos[1])
    elif direction == 'R':
        new_xpos = (xpos[0], xpos[1]+1)
    elif direction == 'L':
        new_xpos = (xpos[0], xpos[1]-1)

def part_one(my_input):
    logger = logging.getLogger("2022:d9:p1")
    size = 10
    grid = []
    initial_val = 0
    grid = [[initial_val for i in range(size)] for j in range(size)]
    grid[0][0] = 1
    hpos = (0, 0)
    tpos = (0, 1)
    for inst in my_input:
        grid, hpos, tpos = walk(grid, inst, hpos, tpos)
    total_spaces = 0
    for row in grid:
        total_spaces += sum()


def part_two(my_input):
    logger = logging.getLogger("2022:d9:p2")


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 123
    # assert part_two(my_input) == 123

    # my_input = parse_file(os.path.join(CWD, "input.txt"))
    # assert part_one(my_input) == 123
    # assert part_two(my_input) == 123
