#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.INFO)
CWD = os.path.dirname(os.path.abspath(__file__))
DAY = CWD.split('/')[-1]
YEAR = CWD.split('/')[-2]

logger = logging.getLogger(f"{YEAR}:d{DAY}")


def parse_file(filename):
    ws = []
    with open(filename, "r") as f:
        for line in f.readlines():
            ws.append(list(line.strip()))
    return ws


def is_word_at_position(ws, start_row, start_col, direction, word='XMAS'):
    rows = len(ws)
    cols = len(ws[0])
    row_diff, col_diff = direction

    for i in range(len(word)):
        r = start_row + (row_diff * i)
        c = start_col + (col_diff * i)
        if not (0 <= r < rows and 0 <= c < cols):
            return False
        elif ws[r][c] != word[i]:
            return False
    return True


def part_one(ws):
    directions = [
        (0, 1),    # right
        (1, 0),    # down
        (1, 1),    # down right
        (1, -1),   # down left
        (0, -1),   # left
        (-1, 0),   # up
        (-1, -1),  # up left
        (-1, 1)    # up-right
    ]
    total = 0
    rows = len(ws)
    cols = len(ws[0])

    for r in range(rows):
        for c in range(cols):
            for direction in directions:
                if is_word_at_position(ws, r, c, direction, word='XMAS'):
                    total += 1
    logger.info(f"total: {total}")
    return total


def is_crossed_word_at_position(ws, rowpos, colpos, word='MAS'):
    if (rowpos == 0) or (colpos == 0) or (rowpos == len(ws)-1) or (colpos == len(ws[0])-1):
        return False  # can't make an X with centre at edges of ws
    slash_chars = [  # / of X
        ws[rowpos+1][colpos-1],  # go down and left
        ws[rowpos][colpos],
        ws[rowpos-1][colpos+1]]  # go up and right
    backslash_chars = [  # \ of X
        ws[rowpos-1][colpos-1],  # go up and left
        ws[rowpos][colpos],
        ws[rowpos+1][colpos+1]]  # go down and right

    test_words = [word, word[::-1]]
    if (''.join(slash_chars) in test_words) and (''.join(backslash_chars) in test_words):
        return True
    return False


def part_two(ws):
    rows = len(ws)
    cols = len(ws[0])

    total = 0
    for r in range(rows):
        for c in range(cols):
            if is_crossed_word_at_position(ws, r, c, word='MAS'):
                logger.debug(f"found at {r}, {c}")
                total += 1
    logger.info(f"total: {total}")
    return total


if __name__ == "__main__":
    logger.info("")
    ws = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(ws) == 18
    assert part_two(ws) == 9

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 2530
    assert part_two(my_input) == 1921
