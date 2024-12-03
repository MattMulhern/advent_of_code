#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = os.path.basename(CWD)

logger = logging.getLogger(f"2024:d{DAY}")


def parse_file(filename):
    reports = []
    with open(filename, "r") as fp:
        for line in fp.readlines():
            splitline = line.strip().split()
            reports.append([int(x) for x in splitline])
    return reports


def part_one(my_input):
    safe_count = 0
    for report in my_input:
        is_safe = report_is_safe(report)
        if is_safe:
            safe_count += 1
    logger.info(f"safe_count: {safe_count}")
    return safe_count


def report_is_safe(report):
    is_increasing = False
    is_decreasing = False
    if report[0] < report[1]:
        is_increasing = True
    else:
        is_decreasing = True
    for i, val in enumerate(report):
        if i == 0:
            post = report[i + 1]
            prev = None
        elif i == (len(report)-1):
            post = None
            prev = report[i - 1]
        else:
            post = report[i + 1]
            prev = report[i - 1]

        if post:
            diff = abs(int(val) - int(post))
            if (diff > 3) or (diff < 1):
                return False
        if prev:
            if (val <= prev) and is_increasing:
                return False  # stopped increasing
            elif (val >= prev) and is_decreasing:
                return False  # stopped decreasing

            diff = abs(int(val) - int(prev))
            if (diff > 3) or (diff < 1):
                return False
    return True


def part_two(my_input):
    safe_count = 0
    for report in my_input:
        if report_is_safe(report):
            safe_count += 1
        else:
            for i, _ in enumerate(report):
                tmp = report.copy()
                tmp.pop(i)
                if report_is_safe(tmp):
                    safe_count += 1
                    break
    logger.info(f"safe_count: {safe_count}")
    return safe_count


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 2
    assert part_two(my_input) == 4

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 299
    assert part_two(my_input) == 364
