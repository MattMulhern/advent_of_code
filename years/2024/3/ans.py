#!/usr/bin/env python3
import logging
import os
import re

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = os.path.basename(CWD)

logger = logging.getLogger(f"2024:d{DAY}")

MUL_RE = re.compile(r"mul\(\d+,\d+\)")


def parse_file(filename):
    with open(filename, "r") as fp:
        return fp.readlines()


def part_one(my_input):
    total = 0
    for line in my_input:
        matches = MUL_RE.findall(line)
        for match in matches:
            vals = [int(x) for x in match.lstrip('mul(').strip(')').split(',')]
            total += (vals[0] * vals[1])
    logger.info(f"part 1 total: {total}")
    return total


def part_two(my_input):
    total = 0
    enabled = True  # mul instructions are enabled by default
    superstring = ''.join(my_input)
    tokens = re.split(r'(do\(\)|don\'t\(\)|mul\(\d+,\d+\))', superstring)

    tokens = [token for token in tokens if token.strip()]  # Remove empty tokens
    # logger.debug(f"tokens: {tokens}")
    for token in tokens:
        # logger.debug(f"processing token: {token}")
        if token == 'do()':
            enabled = True
        elif token == "don't()":
            enabled = False
        elif MUL_RE.match(token):
            if enabled:
                vals = [int(x) for x in token.lstrip('mul(').rstrip(')').split(',')]
                # logger.debug(f"using {token} as {vals}")
                total += (vals[0] * vals[1])
            # else:
            #     logger.debug(f"skipping disabled {token}")
        # else:
        #     logger.debug(f"skipping junk {token}")
    logger.info(f"part 2 total: {total}")
    return total


if __name__ == "__main__":
    example_str = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    assert part_one([example_str]) == 161
    example_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    assert part_two([example_str]) == 48

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 170068701
    assert part_two(my_input) == 78683433
