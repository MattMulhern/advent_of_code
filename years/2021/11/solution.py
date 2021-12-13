#!/usr/bin/env python3
import logging
import os
import aoc

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d11')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def flash_surrounding(flash):
    flashed = []
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (+1, 0), (1, 1)]

    for direction in directions:
        i = direction[0] + flash[0]
        j = direction[1] + flash[1]
        if 0 <= i < 10 and 0 <= j < 10 and grid[i][j] != 10:
            grid[i][j] += 1
            if grid[i][j] == 10:
                flashed.append((i, j))
    return flashed


def iterate(grid):
    total_flashes = 0
    iterations = 0

    while True:
        flashed = []
        for y in range(10):
            for x in range(10):
                grid[y][x] += 1
                if grid[y][x] == 10:
                    flashed.append((y, x))
        for flash in flashed:
            flashed += flash_surrounding(flash)
        total_flashes += len(flashed)
        iterations += 1

        if iterations == 100:
            flashes_after_100_iterations = total_flashes

        if len(flashed) == 100:
            return flashes_after_100_iterations, iterations

        for y, x in flashed:
            grid[y][x] = 0


if __name__ == "__main__":

    grid = aoc.file_to_2d_list_of_ints(os.path.join(CWD, 'example.txt'))
    flashes_after_100_iterations, iterations_until_sync = iterate(grid)
    logger.info(f"flashes after 100 iterations: {flashes_after_100_iterations}")
    logger.info(f"iterations until synchronization: {iterations_until_sync}")
    assert flashes_after_100_iterations == 1656
    assert iterations_until_sync == 195

    grid = aoc.file_to_2d_list_of_ints(os.path.join(CWD, 'input.txt'))
    flashes_after_100_iterations, iterations_until_sync = iterate(grid)
    logger.info(f"flashes after 100 iterations: {flashes_after_100_iterations}")
    logger.info(f"iterations until synchronization: {iterations_until_sync}")
    assert flashes_after_100_iterations == 1620
    assert iterations_until_sync == 371
