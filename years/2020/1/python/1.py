#!/usr/bin/env python
def part_one(lines):
    """ my correct answer was 703131 """
    print("*** PART 1 ***")
    for numa in lines:
        for numb in lines:
            if int(numa) + int(numb) == 2020:
                pair = (int(numa), int(numb))
                break
    print(f"{pair[0]} + {pair[1]} = 2020")
    print(f"{pair[0]} * {pair[1]} = {pair[0] * pair[1]}")


def part_two(lines):
    """ my correct answer was 272423970 """
    print("*** PART 2 ***")
    for numa in lines:
        for numb in lines:
            for numc in lines:
                if int(numa) + int(numb) + int(numc) == 2020:
                    pair = (int(numa), int(numb), int(numc))
                    break
    print(f"{pair[0]} + {pair[1]} + {pair[2]} += 2020")
    print(f"{pair[0]} * {pair[1]} * {pair[2]} = {pair[0] * pair[1] * pair[2]}")


if __name__ == "__main__":
    with open("../1.input.txt", "r") as fp:
        lines = fp.readlines()
        part_one(lines)
        part_two(lines)
