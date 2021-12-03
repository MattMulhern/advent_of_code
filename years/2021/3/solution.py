#!/usr/bin/env python3
import logging
import aoc
import os
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d3')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def part_one(report):
    gamma_bits = []   # most common
    epsilon_bits = []  # least common
    for col, _ in enumerate(report[0]):
        bits_in_position = []
        for line in report:
            bits_in_position.append(line[col])
        ctr = Counter(bits_in_position).most_common()
        gamma_bits.append(ctr[0][0])
        epsilon_bits.append(ctr[-1][0])
    gamma = int(''.join(gamma_bits), 2)
    epsilon = int(''.join(epsilon_bits), 2)
    product = gamma * epsilon
    logger.info(f"{gamma} * {epsilon} = {product}")
    return product


def filter_by_column(report, column, mode='most'):
    new_report = []
    bits_in_col = [x[column] for x in report]
    ctr = Counter(bits_in_col).most_common()

    if ctr[0][1] == ctr[1][1]:  # if there is a draw in counts:
        if mode == 'most':
            wanted = '1'
        elif mode == 'least':
            wanted = '0'
        else:
            raise ValueError('Bad mode!')
    else:
        if mode == 'most':
            wanted = ctr[0][0]
        elif mode == 'least':
            wanted = ctr[-1][0]
        else:
            raise ValueError('Bad mode!')

    for line in report:
        if line[column] in wanted:
            new_report.append(line)
    return new_report


def get_oxygen_rating(report):
    column = 0
    while len(report) != 1:
        if column >= len(report[0]):
            raise ValueError('COULDNT FIND!!')
        report = filter_by_column(report, column, mode='most')
        column += 1
    return report[0]


def get_co2_rating(report):
    column = 0
    while len(report) != 1:
        if column >= len(report[0]):
            raise ValueError('COULDNT FIND!!')
        report = filter_by_column(report, column, mode='least')
        column += 1
    return report[0]


def part_two(report):
    oxygen_rating_binary = get_oxygen_rating(report)
    co2_rating_binary = get_co2_rating(report)

    oxygen_rating = int(oxygen_rating_binary, 2)
    co2_rating = int(co2_rating_binary, 2)

    product = oxygen_rating * co2_rating
    logger.info(f"{oxygen_rating} * {co2_rating} = {product}")
    return product


if __name__ == "__main__":
    logger.info('example.txt')
    report = aoc.file_to_list_of_strings(os.path.join(CWD, 'example.txt'))
    assert part_one(report) == 198
    assert part_two(report) == 230
    logger.info('input.txt')
    report = aoc.file_to_list_of_strings(os.path.join(CWD, 'input.txt'))
    assert part_one(report) == 3242606
    assert part_two(report) == 4856080
