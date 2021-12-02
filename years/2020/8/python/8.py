#!/usr/bin/env python


def part_one(instructions):
    print("*** PART 1 ***")
    idx_dict = {}
    for x in range(len(instructions)):
        idx_dict[x] = False

    acc, idx = operate(0, 0, instructions)

    while True:
        new_acc, new_idx = operate(acc, idx, instructions)
        if idx_dict[new_idx]:
            break
        idx_dict[new_idx] = True
        acc = new_acc
        idx = new_idx
    print(f"The last value of acc BEFORE reaching the starting point is {acc}")
    return acc


def do_nop(acc, idx, instructions):
    return acc, idx+1


def do_acc(acc, idx, instructions):
    return acc+instructions[idx][1], idx+1


def do_jmp(acc, idx, instructions):
    # import pdb; pdb.set_trace()
    return acc, idx+instructions[idx][1]


def operate(acc, idx, instructions):
    # print(f"acc={acc}, idx={idx} operating on {instructions[idx]}")
    if instructions[idx][0] == 'nop':
        return do_nop(acc, idx, instructions)
    elif instructions[idx][0] == 'acc':
        return do_acc(acc, idx, instructions)
    elif instructions[idx][0] == 'jmp':
        return do_jmp(acc, idx, instructions)
    else:
        return ValueError(f"Got bad instruction {instructions[idx]}")


def is_infinite(instructions):
    idx_dict = {}
    for x in range(len(instructions)):
        idx_dict[x] = False

    acc, idx = operate(0, 0, instructions)

    while True:
        new_acc, new_idx = operate(acc, idx, instructions)
        if new_idx not in idx_dict.keys():
            return False, new_acc  # we want the acc AFTER the operation here
        if idx_dict[new_idx]:
            return True, acc  # we want the acc BEFORE the operation here

        idx_dict[new_idx] = True
        acc = new_acc
        idx = new_idx


def part_two(instructions):
    print("*** PART 2 ***")
    for idx, instruction in enumerate(instructions):
        new_instructions = instructions.copy()
        # print(f"trying flipping instruction {idx}: {instruction}")
        new_instruction = flip_instruction(instruction)
        new_instructions[idx] = new_instruction
        is_inf, acc = is_infinite(new_instructions)
        if is_inf is False:
            print(f"Flipping instruction {idx}: {instruction} successfully exits with acc={acc}")
            return acc
    print("Could not fix the boot program by flipping any instructions! :(")


def flip_instruction(instruction):
    if instruction[0] == 'acc':
        return instruction
    elif instruction[0] == 'nop':
        return ('jmp', instruction[1])
    elif instruction[0] == 'jmp':
        return ('nop', instruction[1])
    else:
        raise ValueError(f"Could not flip instruction: {instruction}")


def parse_input(lines):
    instructions = []
    for line in lines:
        op = line.split()[0]
        val = line.split()[1]
        instructions.append((op, int(val)))
    return instructions


if __name__ == "__main__":
    print("*** EXAMPLE ***")
    with open("../8.example.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        instructions = parse_input(lines)
        assert part_one(instructions) == 5
        assert part_two(instructions) == 8

    print("\n*** MY INPUT ***")
    with open("../8.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        instructions = parse_input(lines)
        assert part_one(instructions) == 1087
        assert part_two(instructions) == 780
