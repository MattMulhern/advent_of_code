#!/usr/bin/env python3
import logging
import os
import re

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    games = {}
    id_re = re.compile(r"Game (\d+):")
    sub_reg = re.compile(r"(\d+) (\w+)")
    with open(filename, "r") as fp:
        for line in fp.readlines():
            game = id_re.findall(line)
            if len(game) > 1:
                raise SystemError(f"failed to get game from {line}")
            id = int(game[0])
            games[id] = []
            substrs = [
                x.lstrip() for x in line.strip().split(":")[-1].lstrip().split(";")
            ]

            for substr in substrs:
                sub = {}
                splits = sub_reg.findall(substr)
                for split in splits:
                    if split[-1] in sub.keys():
                        raise SystemError(f"duplicate colour in sub? {line} [{substr}]")
                    else:
                        sub[split[-1]] = int(split[0])
                games[id].append(sub)
        return games


def is_game_valid(requirements, game):
    for sub in game:
        for req, reqval in requirements.items():
            if req not in sub.keys():
                continue
            if sub[req] > reqval:
                return False
    return True


def part_one(my_input):
    logger = logging.getLogger("2022:d2:p1")
    total = 0
    for id, game in my_input.items():
        if is_game_valid({"red": 12, "green": 13, "blue": 14}, game):
            total += id
    logger.info(f"total of ids is {total}")
    return total


def part_two(my_input):
    logger = logging.getLogger("2022:d2:p2")
    total = 0
    for game in my_input.values():
        max_cubes = {"red": 0, "green": 0, "blue": 0}
        for sub in game:
            for colour, val in sub.items():
                if val > max_cubes[colour]:
                    max_cubes[colour] = val
        game_product = max_cubes["red"] * max_cubes["green"] * max_cubes["blue"]
        total += game_product
    logger.info(f"total of products is {total}")
    return total


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 8
    assert part_two(my_input) == 2286

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 2283
    assert part_two(my_input) == 78669
