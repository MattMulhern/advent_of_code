#!/usr/bin/env python
def part_one(lines):
    """ my correct answer was 580 """
    print("*** PART 2 ***")
    valid_count = 0
    for line in lines:
        splitline = line.strip().split()
        char = splitline[1].strip(":")
        ranges = [int(x) for x in splitline[0].split("-")]
        password = splitline[-1]
        if (password.count(char) >= ranges[0]) and (password.count(char) <= ranges[1]):
            valid_count += 1
    print(f"There are {valid_count} valid passwords")


def part_two(lines):
    """ my correct answer was 611 """
    print("*** PART 2 ***")
    valid_count = 0
    for line in lines:
        splitline = line.strip().split()
        char = splitline[1].strip(":")
        positions = [int(x) for x in splitline[0].split("-")]
        password = splitline[-1]

        at_position_count = 0
        for position in positions:
            if (
                password[position - 1] == char
            ):  # "Toboggan Corporate Policies have no concept of "index zero"!"
                at_position_count += 1
        if at_position_count == 1:
            valid_count += 1
    print(f"There are {valid_count} valid passwords")


if __name__ == "__main__":
    with open("../2.input.txt", "r") as fp:
        lines = fp.readlines()
        part_one(lines)
        part_two(lines)
