#!/usr/bin/env python3
import logging
import os
import re
import numpy as np

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


def parse_file(filename):
    inst_re = re.compile(r"move\s*([0-9]*)\s*from\s([0-9]*)\s*to\s*([0-9]*)")
    chunk_size = 4
    state = []
    instructions = []
    with open(filename, "r") as fp:
        raw = fp.read()
        state_raw, inst_raw = raw.split("\n\n")
        state_lines = state_raw.split("\n")

        for line in state_lines[:-1]:
            chunked = []
            for i in range(0, len(line), chunk_size):
                chunk = line[i: i + chunk_size]
                chunked.append(chunk.strip().lstrip("[").rstrip("]"))
            state.append(chunked)

        state.reverse()
        state = np.transpose(state).tolist()

        for line in inst_raw.split("\n"):
            inst = inst_re.search(line).groups()
            inst = [int(x) for x in inst]
            inst[1] -= 1
            inst[2] -= 1
            instructions.append(tuple(inst))

    return state, instructions


def part_one(state, instructions):
    logger = logging.getLogger("2022:d5:p1")
    for instruction in instructions:
        state = move_crates(state, instruction)
    ret_code = []
    for stack in state:
        top_idx, top_val = get_top_crate(stack)
        ret_code.append(top_val)
    ret_str = "".join(ret_code)
    logger.info(f"final code: {ret_str}")
    return ret_str


def get_top_space(stack):
    for idx, val in enumerate(stack):
        if val == "":
            return idx
    return len(stack)  # grow the stack


def get_top_crate(stack):
    if stack[0] == "":
        return 0, ""
        # raise ValueError(f"looking for top crate in empty stack: {stack}")
    for idx, val in enumerate(stack):
        if val == "":
            return idx - 1, stack[idx - 1]
    return len(stack) - 1, stack[-1]


def move_crates(state, instruction, multistack=False):
    if multistack:
        state = move_crate_stack(state, instruction[1], instruction[2], instruction[0])
    else:
        for _ in range(0, instruction[0]):
            state = move_crate(state, instruction[1], instruction[2])
    return state


def move_crate(state, src, dest):
    src_top_idx, src_top_val = get_top_crate(state[src])
    dest_space_idx = get_top_space(state[dest])
    if len(state[dest]) == dest_space_idx:
        state[dest].append(src_top_val)
    else:
        state[dest][dest_space_idx] = src_top_val
    state[src][src_top_idx] = ""
    return state


def move_crate_stack(state, src, dest, size):
    src_top_start, src_top_values = get_top_crates(state[src], size)
    dest_space_idx = get_top_space(state[dest])
    for idx, val in enumerate(src_top_values):
        dest_idx = dest_space_idx + idx
        if len(state[dest]) == dest_idx:
            state[dest].append(val)
        else:
            state[dest][dest_idx] = val
    for idx, val in enumerate(src_top_values, start=src_top_start):
        state[src][idx] = ""
    return state


def get_top_crates(stack, size):
    if size == 1:
        idx, val = get_top_crate(stack)
        return idx, val

    for idx, val in enumerate(stack):
        if val == "":
            return idx - size, stack[idx - size: idx]
    return len(stack) - size, stack[len(stack) - size: len(stack)]


def part_two(state, instructions):
    logger = logging.getLogger("2022:d5:p2")
    for instruction in instructions:
        state = move_crates(state, instruction, multistack=True)

    ret_code = []

    for stack in state:
        top_idx, top_val = get_top_crate(stack)
        ret_code.append(top_val)
    ret_str = "".join(ret_code)
    logger.info(f"final code: {ret_str}")
    return ret_str


if __name__ == "__main__":
    initial_state, instructions = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(initial_state, instructions) == "CMZ"
    initial_state, instructions = parse_file(os.path.join(CWD, "example.txt"))
    assert part_two(initial_state, instructions) == "MCD"

    initial_state, instructions = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(initial_state, instructions) == "FCVRLMVQP"
    initial_state, instructions = parse_file(os.path.join(CWD, "input.txt"))
    assert part_two(initial_state, instructions) == "RWLWGJGFD"
