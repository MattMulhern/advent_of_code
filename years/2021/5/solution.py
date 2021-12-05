#!/usr/bin/env python3
import logging
import os
import re
import numpy as np

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('2021:d5')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))
VENT_RE = re.compile(r'(\d*),(\d*) -> (\d*),(\d*)')


def parse_vent_file(filename):
    vents = []
    max_size = 0
    with open(filename, 'r') as fp:
        logger.info(f"parsing {filename}")
        lines = [x.strip() for x in fp.readlines()]
        for line in lines:
            vent = VENT_RE.match(line)
            if vent:
                vent = [int(x) for x in vent.groups()]
                if max(vent) > max_size:
                    max_size = max(vent)
                vents.append(((vent[0], vent[1]), (vent[2], vent[3])))
        return vents, max_size


def walk(start, finish):
    if start < finish:
        return [x for x in range(start, finish+1)]
    return [x for x in range(start, finish-1, -1)]


def part_one(vents, max_size):
    arr_size = max_size+1
    arr = np.zeros(dtype=np.int8, shape=(arr_size, arr_size))
    for vent in vents:
        # x val constant, vertical vent
        if vent[0][0] == vent[1][0]:
            if vent[0][1] > vent[1][1]:  # vent given backwards, reverse order for range()
                vent = (vent[1], vent[0])

            x = vent[0][0]
            for y in range(vent[0][1], vent[1][1]+1):  # +1 to include end point of vent
                arr[y][x] += 1

        # y val constant, horizontal vent
        elif vent[0][1] == vent[1][1]:
            if vent[0][0] > vent[1][0]:  # vent given backwards, reverse order for range()
                vent = (vent[1], vent[0])

            y = vent[0][1]
            for x in range(vent[0][0], vent[1][0]+1):  # +1 to include end point of vent
                arr[y][x] += 1

    points = 0
    for row in arr:
        for val in row:
            if val > 1:
                points += 1
    logger.info(f"total_points: {points}")
    return points


def part_two(vents, max_size):
    arr_size = max_size+1
    arr = np.zeros(dtype=np.int8, shape=(arr_size, arr_size))

    for vent in vents:
        x1, y1, x2, y2 = vent[0][0], vent[0][1], vent[1][0], vent[1][1]
        # x val constant, vertical vent
        if vent[0][0] == vent[1][0]:
            x = vent[0][0]
            points_to_increment = [(x, y) for y in walk(y1, y2)]
            for point in points_to_increment:
                arr[point[1]][point[0]] += 1

        # y val constant, horizontal vent
        elif vent[0][1] == vent[1][1]:
            y = vent[0][1]
            points_to_increment = [(x, y) for x in walk(x1, x2)]
            for point in points_to_increment:
                arr[point[1]][point[0]] += 1

        # nothing constant, diagonal
        else:
            # logger.debug(vent)
            points_to_increment = zip(walk(x1, x2), walk(y1, y2))
            for point in points_to_increment:
                arr[point[1]][point[0]] += 1

    points = 0
    for row in arr:
        for val in row:
            if val > 1:
                points += 1
    logger.info(f"total_points: {points}")
    return points


if __name__ == "__main__":
    logger.info('example.txt')
    vents, max_size = parse_vent_file(os.path.join(CWD, 'example.txt'))
    assert part_one(vents, max_size) == 5
    assert part_two(vents, max_size) == 12
    logger.info('input.txt')
    vents, max_size = parse_vent_file(os.path.join(CWD, 'input.txt'))
    assert part_one(vents, max_size) == 7674
    assert part_two(vents, max_size) == 20898
