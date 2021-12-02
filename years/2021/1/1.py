#!/usr/bin/env python3
import logging
import aoc
import os

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('2021:d1')

CWD = os.path.dirname(os.path.abspath(__file__))


def part_one(depths):
    logger.info("*** PART 1 ***")
    num_increases = 0
    previous = depths[0]
    for depth in depths[1:]:
        if depth > previous:
            num_increases += 1
        previous = depth
    logger.info(f"The depth increased {num_increases} times.")
    return num_increases


def part_two(depths):
    logger.info("*** PART 2 ***")
    num_increases = 0
    previous = sum(depths[:3])
    for i, _ in enumerate(depths):
        try:
            val = sum(depths[i:i+3])
            if val > previous:
                num_increases += 1
            previous = val
        except IndexError:
            break
    logger.info(f"The depth increased {num_increases} times.")
    return num_increases


if __name__ == "__main__":
    logger.info('example.txt')
    depths = aoc.file_to_list_of_ints(os.path.join(CWD, 'example.txt'))
    assert part_one(depths) == 7
    assert part_two(depths) == 5

    logger.info('input.txt')
    depths = aoc.file_to_list_of_ints(os.path.join(CWD, 'input.txt'))
    assert part_one(depths) == 1692
    assert part_two(depths) == 1724
