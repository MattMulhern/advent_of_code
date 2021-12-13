#!/usr/bin/env python3
import logging
import os
from collections import defaultdict


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('2021:d12')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def parse_cave_file(filename):
    logger.info(f"parsing {filename}")
    with open(filename, 'r') as fp:
        return [tuple(x.strip().split('-')) for x in fp.readlines()]


def find_paths(current, neighbours, small_caves, visited):
    if (current in visited):
        return 0
    if (current == 'end'):
        return 1
    if (current in small_caves):
        visited.add(current)

    total_paths = 0

    for neighbour in neighbours[current]:
        total_paths += find_paths(neighbour, neighbours, small_caves, visited)

    visited.discard(current)

    return total_paths


def part_one(links):
    neighbours = defaultdict(list)
    small_caves = set()
    for link in links:
        neighbours[link[0]].append(link[1])
        neighbours[link[1]].append(link[0])

        if (link[0].lower() == link[0]):
            small_caves.add(link[0])
        if (link[1].lower() == link[1]):
            small_caves.add(link[1])
    total_paths = find_paths('start', neighbours, small_caves, set())
    logger.info(f"total paths: {total_paths}")
    return total_paths


def find_paths_visiting_small_caves_twice(current, neighbours, small_caves, visited, visited_small_twice):
    if (current == 'end'):
        return 1
    if (visited[current] > 0 and visited_small_twice):
        return 0
    if (current in small_caves):
        visited[current] += 1
        if visited[current] == 2:
            visited_small_twice = True

    total_paths = 0
    for neighbor in neighbours[current]:
        if (neighbor != 'start'):
            total_paths += find_paths_visiting_small_caves_twice(neighbor, neighbours, small_caves, visited, visited_small_twice)

    visited[current] -= 1

    return total_paths


def part_two(links):
    neighbours = defaultdict(list)
    small_caves = set()
    for link in links:
        neighbours[link[0]].append(link[1])
        neighbours[link[1]].append(link[0])

        if (link[0].lower() == link[0]):
            small_caves.add(link[0])
        if (link[1].lower() == link[1]):
            small_caves.add(link[1])

    total_paths = find_paths_visiting_small_caves_twice('start', neighbours, small_caves, defaultdict(int), False)
    logger.info(f"total paths: {total_paths}")
    return total_paths


if __name__ == "__main__":
    links = parse_cave_file(os.path.join(CWD, 'example.txt'))
    assert part_one(links) == 10
    assert part_two(links) == 36
    links = parse_cave_file(os.path.join(CWD, 'input.txt'))
    assert part_one(links) == 3485
    assert part_two(links) == 85062
