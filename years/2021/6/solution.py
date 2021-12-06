#!/usr/bin/env python3
import logging
import os
import aoc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d6')
logger.setLevel(logging.INFO)

CWD = os.path.dirname(os.path.abspath(__file__))


def update_school(school):
    new_school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}

    for day in range(8, 0, -1):
        new_school[day-1] = school[day]

    # handle births at day 0
    new_school[6] += school[0]
    new_school[8] += school[0]

    return new_school


def breed(initial, days=80):
    school = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
    for fish in initial:
        school[fish] += 1
    logger.debug(f"Initial state: {school}")
    for day in range(1, days+1):
        school = update_school(school)
        total = sum(school.values())
        logger.debug(f"after {day} days: [{total}]")
    logger.info(f"total after {days} days: {total}")
    return sum(school.values())


if __name__ == "__main__":
    logger.info('example.txt')
    school = aoc.file_to_list_of_int_lists(os.path.join(CWD, 'example.txt'))[0]
    assert breed(school, days=80) == 5934
    assert breed(school, days=256) == 26984457539
    logger.info('input.txt')
    school = aoc.file_to_list_of_int_lists(os.path.join(CWD, 'input.txt'))[0]
    assert breed(school, days=80) == 374994
    assert breed(school, days=256) == 1686252324092
