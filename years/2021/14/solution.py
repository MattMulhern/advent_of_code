#!/usr/bin/env python3
import logging
import os
from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d14')
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


def grow_by_count(poly, rules, iterations):
    element_counter = Counter(poly)
    pairs = Counter(poly[i:i + 2] for i in range(len(poly) - 1))

    for step in range(iterations):
        new_poly = Counter()
        for pair, count in pairs.items():
            if pair in rules:
                left, right = pair
                new_poly[pair[0] + rules[pair]] += count
                new_poly[rules[pair] + pair[1]] += count
                element_counter[rules[pair]] += count
            else:
                new_poly[pair] = count
        pairs = new_poly
    return element_counter


def part_two(poly, rules):
    element_counter = grow_by_count(poly, rules, 40)
    ordered = element_counter.most_common()
    diff = ordered[0][1] - ordered[-1][1]
    logger.info(f"{ordered[0][0]}({ordered[0][1]}) - {ordered[-1][0]}({ordered[-1][1]}) = {diff}")
    return diff


if __name__ == "__main__":
    template, rules = parse_ploymer(os.path.join(CWD, 'example.txt'))
    assert part_one(template, rules) == 1588
    assert part_two(template, rules) == 2188189693529
    template, rules = parse_ploymer(os.path.join(CWD, 'input.txt'))
    assert part_one(template, rules) == 2003
    assert part_two(template, rules) == 2276644000111
