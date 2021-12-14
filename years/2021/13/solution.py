#!/usr/bin/env python3
import logging
import os
import ipdb
import numpy as np

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d13')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def parse_folding_instructions(filename):
    logger.info(f"parsing {filename}")
    dots = []
    instructions = []
    with open(filename, 'r') as fp:
        dots_str, instructions_str = fp.read().split('\n\n')
        for line in dots_str.split():
            dot = tuple(int(x) for x in line.split(','))
            dots.append(dot)
        for line in instructions_str.split('\n'):
            split_line = line.removeprefix('fold along ').split('=')
            ipdb
            instructions.append((split_line[0], int(split_line[1])))
    return dots, instructions


def fold_paper(page, fold_line, axis):
    if axis == 'x':
        paper_back = page[:fold_line, :].copy()
        paper_front = page[fold_line+1:, :].copy()
        folded_page = np.flip(paper_front, axis=0) + paper_back
    elif axis == 'y':
        paper_back = page[:, :fold_line].copy()
        paper_front = page[:, fold_line+1:].copy()
        folded_page = np.flip(paper_front, axis=1) + paper_back
    folded_page = np.where(folded_page > 1, 1, folded_page)  # reset values >1 to 1
    return folded_page


def part_one(dots, instructions):
    x_max = max([x[0] for x in dots])
    y_max = max([x[1] for x in dots])
    page = np.zeros((x_max + 1, y_max + 1), dtype=int)
    for dot in dots:
        page[dot[0]][dot[1]] += 1

    page = fold_paper(page, instructions[0][1], instructions[0][0])
    total_dots = page.sum()

    logger.info(f"total dots after 1 fold: {total_dots}")
    return total_dots


def part_two(dots, instructions):
    x_max = max([x[0] for x in dots])
    y_max = max([x[1] for x in dots])
    page = np.zeros((x_max + 1, y_max + 1), dtype=int)
    for dot in dots:
        page[dot[0]][dot[1]] += 1
    for instruction in instructions:
        page = fold_paper(page, instruction[1], instruction[0])

    page = page.transpose()
    page = page.astype(str)
    page = np.where(page == '0', ' ', page)
    logger.info("Code below:")
    for row in page:
        logger.info(''.join(row))


if __name__ == "__main__":
    dots, instructions = parse_folding_instructions(os.path.join(CWD, 'example.txt'))
    assert part_one(dots, instructions) == 17
    part_two(dots, instructions)

    dots, instructions = parse_folding_instructions(os.path.join(CWD, 'input.txt'))
    assert part_one(dots, instructions) == 765
    part_two(dots, instructions)
