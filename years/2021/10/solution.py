#!/usr/bin/env python3
import logging
import os
import aoc
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d10')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))

openers = {'<': '>', '(': ')', '[': ']', '{': '}'}
closers = {'>': '<', ')': '(', ']': '[', '}': '{'}
corrupted_scores = {'>': 25137, ')': 3, ']': 57, '}': 1197}
incomplete_scores = {'>': 4, ')': 1, ']': 2, '}': 3}


def find_corrupted(line):
    chunk = []
    for char in line:
        if char in openers:
            chunk.append(char)
        elif char in closers and chunk[-1] == closers[char]:
            chunk.pop()
        else:
            return char


def part_one(lines):
    total_score = 0
    for row in lines:
        corrupted_char = find_corrupted(row)
        if corrupted_char:
            total_score += corrupted_scores[corrupted_char]
    logger.info(f"corrupted total score: {total_score}")
    return total_score


def complete(line):
    chunk = []
    for char in line:
        if char in openers:
            chunk.append(char)
        elif char in closers and chunk[-1] == closers[char]:
            chunk.pop()
        else:
            raise RuntimeError('FOUND CORRUPTED!?')  # we should never get in here

    if len(chunk) == 0:
        logger.debug('row complete')
        return 0

    chunk_score = 0
    chunk.reverse()

    for char in chunk:
        char_score = incomplete_scores[openers[char]]
        chunk_score = (chunk_score * 5) + char_score

    return chunk_score


def part_two(lines):
    complete_scores = []
    for row in lines:
        corrupted_char = find_corrupted(row)
        if corrupted_char:
            continue
        complete_scores.append(complete(row))

    complete_scores.sort()

    median_score = int(np.median(complete_scores))
    logger.info(f"median compete score: {median_score}")
    return median_score


if __name__ == "__main__":
    lines = aoc.file_to_list_of_strings(os.path.join(CWD, 'example.txt'))
    assert part_one(lines) == 26397
    assert part_two(lines) == 288957
    lines = aoc.file_to_list_of_strings(os.path.join(CWD, 'input.txt'))
    assert part_one(lines) == 413733
    assert part_two(lines) == 3354640192
