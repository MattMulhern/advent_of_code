#!/usr/bin/env python3
import logging
import os
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d12')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def parse_ploymer(filename):
    logger.info(f"parsing {filename}")
    with open(filename, 'r') as fp:
        template, rules = fp.read().split('\n\n')
        rules = rules.split('\n')
        rules_dict = {}
        for rule in rules:
            rule = rule.split(' -> ')
            rules_dict[rule[0]] = rule[1]

    return template, rules_dict


def part_one(poly, rules):
    for iteration in range(1, 11):
        poly = grow_polymer(poly, rules)
    counter = Counter(poly)
    diff = counter.most_common()[0][1] - counter.most_common()[-1][1]
    logger.info(f"{counter.most_common()[0][1]} - {counter.most_common()[-1][1]} = {diff}")
    return diff


def grow_polymer(poly, rules):
    new_poly = []
    for i, _ in enumerate(poly):
        new_poly.append(poly[i])
        if i+1 < len(poly):
            pair = f"{poly[i]}{poly[i+1]}"
            if pair in rules.keys():
                new_poly.append(rules[pair])
    return ''.join(new_poly)


if __name__ == "__main__":
    template, rules = parse_ploymer(os.path.join(CWD, 'example.txt'))
    assert part_one(template, rules) == 1588
    template, rules = parse_ploymer(os.path.join(CWD, 'input.txt'))
    assert part_one(template, rules) == 1588
