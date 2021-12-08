#!/usr/bin/env python3
import logging
import os
import aoc
import numpy as np
import sys
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d7')
logger.setLevel(logging.INFO)

CWD = os.path.dirname(os.path.abspath(__file__))


def part_one(crabs):
    median = int(np.median(crabs))
    fuel_spent = 0
    for crab in crabs:
        fuel_spent += int(abs(crab - median))
    logger.info(f"fuel spent to get to {median}: {fuel_spent}")
    return fuel_spent


def part_two(crabs):
    lowest_fuel = sys.maxsize
    lowest_fuel_pos = 0
    for position, _ in enumerate(crabs):
        logger.debug(f"checking position {position}")
        fuel = calc_fuel_for_position(crabs, position)
        if fuel < lowest_fuel:
            lowest_fuel = fuel
            lowest_fuel_pos = position
        logger.debug(f"fuel for position {position}: {fuel}")
    logger.debug(f"lowest fuel is {lowest_fuel} at position {lowest_fuel_pos}")
    return lowest_fuel


def calc_fuel_for_position(crabs, position):
    fuel_spent = 0
    for crab in crabs:
        distance = abs(crab - position)
        fuel_spent += sum([x for x in range(1, distance+1)])
    return fuel_spent


if __name__ == "__main__":
    logger.info('example.txt')
    crabs = aoc.file_to_list_of_int_lists(os.path.join(CWD, 'example.txt'))[0]
    assert part_one(crabs) == 37
    assert part_two(crabs) == 168
    logger.info('input.txt')
    crabs = aoc.file_to_list_of_int_lists(os.path.join(CWD, 'input.txt'))[0]
    assert part_one(crabs) == 328187
    assert part_two(crabs) == 91257582
