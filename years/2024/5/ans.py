#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = CWD.split('/')[-1]
YEAR = CWD.split('/')[-2]

logger = logging.getLogger(f"{YEAR}:d{DAY}")


def parse_file(filename):
    with open(filename, "r") as f:
        deps = []
        updates = []
        for i, line in enumerate(f.readlines(), start=1):
            if '|' in line:
                deps.append(line.strip().split('|'))
            elif ',' in line:
                updates.append(line.strip().split(','))
            else:
                logger.warning(f"ignoring file line {i}: {line}")
        return deps, updates


def check_update_against_rules(update, rules):
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            if update.index(rule[0]) > update.index(rule[1]):
                return False
    return True


def get_middle_val(update):
    if len(update) % 2 == 0:
        raise ValueError("update must have an odd number of elements!")
    middle_index = len(update) // 2
    return int(update[middle_index])


def part_one(deps, updates):
    total = 0
    for update in updates:
        if check_update_against_rules(update, deps):
            logger.debug(f"update {update} is valid!")
            total += get_middle_val(update)
        else:
            logger.debug(f"update {update} is invalid!")
    logger.info(f"total: {total}")
    return total


def fix_update(update, rules):
    dep_graph = {}  # list of deps of X
    dep_rank = {}  # rank of X
    pages = set(update)

    for x, y in rules:
        if x in pages and y in pages:
            if x not in dep_graph:
                dep_graph[x] = []
            dep_graph[x].append(y)
            if y not in dep_rank:
                dep_rank[y] = 0
            dep_rank[y] += 1  # y comes after x, increment y's rank
            if x not in dep_rank:
                dep_rank[x] = 0

    queue = []
    for page in update:
        if dep_rank.get(page, 0) == 0:
            queue.append(page)  # pages with nothing to their left

    new_update = []
    while queue:
        node = queue.pop(0)
        new_update.append(node)
        for neighbor in dep_graph.get(node, []):
            dep_rank[neighbor] -= 1
            if dep_rank[neighbor] == 0:
                queue.append(neighbor)

    return new_update


def part_two(deps, updates):
    total = 0
    for update in updates:
        if check_update_against_rules(update, deps):
            logger.debug(f"update {update} is valid, skipping!")
        else:
            new_update = fix_update(update, deps)
            logger.debug(f"update corrected from {update} to {new_update}")
            total += get_middle_val(new_update)
    logger.info(f"total: {total}")
    return total


if __name__ == "__main__":
    logger.info("")
    deps, updates = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(deps, updates) == 143
    assert part_two(deps, updates) == 123

    deps, updates = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(deps, updates) == 4872
    assert part_two(deps, updates) == 5564
