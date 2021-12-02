#!/usr/bin/env python3
import logging
import aoc
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('2021:d2')

CWD = os.path.dirname(os.path.abspath(__file__))


def part_one(instructions):
    logger.info("*** PART 1 ***")
    depth = 0
    horizontal = 0
    for instruction in instructions:
        val = int(instruction[1])
        if instruction[0] == 'forward':
            horizontal += val
        elif instruction[0] == 'down':
            depth += val
        elif instruction[0] == 'up':
            depth -= val
        else:
            raise ValueError(f"Could not understand instruction: {instruction}")
    product = depth * horizontal
    logger.info(f"{depth} * {horizontal} = {product}")
    return product


def part_two(depths):
    logger.info("*** PART 2 ***")
    depth = 0
    horizontal = 0
    aim = 0
    for instruction in instructions:
        val = int(instruction[1])
        if instruction[0] == 'forward':
            horizontal += val
            depth += (aim * val)
        elif instruction[0] == 'down':
            aim += val
        elif instruction[0] == 'up':
            aim -= val
        else:
            raise ValueError(f"Could not understand instruction: {instruction}")
    product = depth * horizontal
    logger.info(f"{depth} * {horizontal} = {product}")
    return product


if __name__ == "__main__":
    logger.info('example.txt')
    instructions = aoc.file_to_list_of_str_tuples(os.path.join(CWD, 'example.txt'))
    assert part_one(instructions) == 150
    assert part_two(instructions) == 900
    logger.info('input.txt')
    instructions = aoc.file_to_list_of_str_tuples(os.path.join(CWD, 'input.txt'))
    assert part_one(instructions) == 1451208
    assert part_two(instructions) == 1620141160
