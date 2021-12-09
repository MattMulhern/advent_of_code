#!/usr/bin/env python3
import logging
import os
import aoc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d8')
logger.setLevel(logging.INFO)

CWD = os.path.dirname(os.path.abspath(__file__))


def get_lowest_points(points):
    lowest_points = []
    points_to_check = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for y, row in enumerate(points):
        for x, point in enumerate(row):
            adjacent_points = []
            point = int(point)
            for mod in points_to_check:
                try:
                    check_x = x + mod[0]
                    check_y = y + mod[1]
                    if not 0 <= check_x < len(row):
                        continue
                    if not 0 <= check_y < len(points):
                        continue
                    adjacent_points.append(int(points[check_y][check_x]))
                except IndexError:
                    continue

            is_lowest = True
            for adjacent in adjacent_points:
                if int(adjacent) <= point:
                    is_lowest = False
            if is_lowest:
                lowest_points.append((point, y, x))

    return lowest_points


def part_one(points):
    logger.info('Part 1')
    lowest_points = get_lowest_points(points)
    total_risk = 0
    for point in lowest_points:
        total_risk += (point[0]+1)
    logger.info(f"total risk: {total_risk}")
    return total_risk


def get_climbing_points(points, x, y, seen):
    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # L, R, U, D
    surrounding = []
    for direction in directions:
        logger.debug(f"going {direction} from {y},{x}")
        dx = x + direction[0]
        dy = y + direction[1]
        if not 0 <= dx < len(points[0]):
            logger.debug(f"going {direction} from {y},{x}: {dy},{dx} out of bounds")
            continue
        if not 0 <= dy < len(points):
            logger.debug(f"going {direction} from {y},{x}: {dy},{dx} out of bounds")
            continue
        if int(points[dy][dx]) == 9:
            logger.debug(f"going {direction} from {y},{x}: {dy},{dx} peak")
            continue
        if int(points[dy][dx]) >= int(points[y][x]):
            logger.debug(f"going {direction} from {y},{x}: {dy},{dx} CLIMBING to {points[dy][dx]}")
            surrounding.append((dy, dx))

    for point in surrounding:
        if point not in seen:
            seen.append(point)
            seen, surrounding = get_climbing_points(points, point[1], point[0], seen)

    return seen, surrounding


def calc_basin_size(points, lowest):
    basin_size = 1  # start at 1 to include lowest point
    lowest_height, lowest_y, lowest_x = lowest
    seen, surrounding = get_climbing_points(points, lowest_x, lowest_y, [])
    basin_size = len(seen) + 1
    logger.debug(f"basin @ {lowest} size: {basin_size}")
    return basin_size


def part_two(points):
    logger.info('Part 2')
    lowest_points = get_lowest_points(points)

    basin_sizes = []
    for point in lowest_points:
        basin_size = calc_basin_size(points, point)
        basin_sizes.append(basin_size)
    basin_sizes.sort()
    product = basin_sizes[-1] * basin_sizes[-2] * basin_sizes[-3]
    logger.info(f"{basin_sizes[-1]} *  {basin_sizes[-2]} * {basin_sizes[-3]} = {product}")
    return product


if __name__ == "__main__":
    points = aoc.file_to_2d_list(os.path.join(CWD, 'example.txt'))
    assert part_one(points) == 15
    assert part_two(points) == 1134
    points = aoc.file_to_2d_list(os.path.join(CWD, 'input.txt'))
    assert part_one(points) == 448
    assert part_two(points) == 1417248
