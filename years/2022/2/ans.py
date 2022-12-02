#!/usr/bin/env python3
import logging
import os
import aoc

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))

beats = {"A": "Y", "B": "Z", "C": "X"}
draws = {"A": "X", "B": "Y", "C": "Z"}
loses = {"A": "Z", "B": "X", "C": "Y"}

win_lose_draw = {
    "AX": "DRAW",
    "AY": "WIN",
    "AZ": "LOSE",
    "BX": "LOSE",
    "BY": "DRAW",
    "BZ": "WIN",
    "CX": "WIN",
    "CY": "LOSE",
    "CZ": "DRAW",
}


def score_round(strat):
    score = 0
    if strat[1] == "X":
        score += 1
    elif strat[1] == "Y":
        score += 2
    elif strat[1] == "Z":
        score += 3

    outcome = win_lose_draw["".join(strat)]
    if outcome == "WIN":
        score += 6
    elif outcome == "DRAW":
        score += 3

    return score


def part_one(strats):
    logger = logging.getLogger("2022:d2:p1")
    total_score = 0
    for strat in strats:
        total_score += score_round(strat)
    logger.info(f"total_score: {total_score}")
    return total_score


def part_two(chunks):
    logger = logging.getLogger("2022:d2:p2")
    total_score = 0
    for strat in strats:
        if strat[1] == "X":
            pick = loses[strat[0]]
        elif strat[1] == "Y":
            pick = draws[strat[0]]
        elif strat[1] == "Z":
            pick = beats[strat[0]]
        total_score += score_round((strat[0], pick))
    logger.info(f"total_score: {total_score}")
    return total_score


if __name__ == "__main__":
    strats = aoc.file_to_list_of_str_tuples(os.path.join(CWD, "example.txt"))
    assert part_one(strats) == 15
    assert part_two(strats) == 12

    strats = aoc.file_to_list_of_str_tuples(os.path.join(CWD, "input.txt"))
    assert part_one(strats) == 10595
    assert part_two(strats) == 9541
