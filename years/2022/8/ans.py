#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    heights = []
    with open(filename, "r") as fp:
        for row in fp.readlines():
            heights.append([int(x) for x in list(row.strip())])
    return heights


def part_one(heights):
    logger = logging.getLogger("2022:d8:p1")
    visible_count = 0
    for ridx, row in enumerate(heights):
        for cidx in range(len(row)):
            if is_visible(heights, ridx, cidx):
                visible_count += 1
    logger.info(f"There are {visible_count} visible trees.")
    return visible_count


def is_visible(heights, row, col):
    tree_height = heights[row][col]
    if row == 0:
        return True
    elif row == (len(heights) - 1):
        return True
    elif col == 0:
        return True
    elif col == (len(heights[0]) - 1):
        return True

    left_trees = heights[row][:col]
    right_trees = heights[row][col + 1:]
    col_vals = [heights[x][col] for x in range(len(heights))]
    above_trees = col_vals[:row]
    below_trees = col_vals[row + 1:]

    from_left, from_right, from_above, from_below = True, True, True, True
    for tree in left_trees:
        if tree >= tree_height:
            from_left = False
    for tree in right_trees:
        if tree >= tree_height:
            from_right = False
    for tree in above_trees:
        if tree >= tree_height:
            from_above = False
    for tree in below_trees:
        if tree >= tree_height:
            from_below = False

    if from_left or from_above or from_below or from_right:
        return True


def get_scenic_score(heights, row, col):
    tree_height = heights[row][col]

    left_trees = heights[row][:col]
    right_trees = heights[row][col + 1:]
    col_vals = [heights[x][col] for x in range(len(heights))]
    above_trees = col_vals[:row]
    below_trees = col_vals[row + 1:]
    left_count, right_count, above_count, below_count = 0, 0, 0, 0
    for tree in reversed(left_trees):  # check from right to left
        left_count += 1
        if tree >= tree_height:
            break
    for tree in right_trees:
        right_count += 1
        if tree >= tree_height:
            break
    for tree in reversed(above_trees):  # check from bottom up
        above_count += 1
        if tree >= tree_height:
            break
    for tree in below_trees:
        below_count += 1
        if tree >= tree_height:
            break

    score = left_count * right_count * above_count * below_count

    return score


def part_two(heights):
    logger = logging.getLogger("2022:d8:p2")
    highest_scenic_score = 0
    highest_scenic_score_row = None
    highest_scenic_score_col = None
    for ridx, row in enumerate(heights):
        for cidx in range(len(row)):
            score = get_scenic_score(heights, ridx, cidx)
            if score > highest_scenic_score:
                highest_scenic_score = score
                highest_scenic_score_col = cidx
                highest_scenic_score_row = ridx
    logger.info(
        f"The highest scenic score is {highest_scenic_score} at ({highest_scenic_score_row}, {highest_scenic_score_col})"
    )
    return highest_scenic_score


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 21
    assert part_two(my_input) == 8

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 1546
    assert part_two(my_input) == 519064
