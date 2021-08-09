#!/usr/bin/env python
def part_one(lines):
    """ my correct answer was 6947 """
    print("*** PART 1 ***")
    total = 0
    for group in groups:
        total += len(set(''.join(group)))
    print(f"the sum of the group entries is {total}")
    return total


def part_two(lines):
    """ my correct answer was 3398 """
    print("*** PART 2 ***")
    total = 0
    for group in groups:
        common_letters = []
        groupstr = sorted(''.join(group))
        for char in groupstr:
            if char in common_letters:
                continue
            if groupstr.count(char) == len(group):
                common_letters.append(char)
        total += len(common_letters)
    print(f"the sum of the group entries is {total}")
    return total


def chunk_lines(lines):
    chunks = []
    chunks.append([])
    chunk_id = 0
    for line in lines:
        if len(line) == 0:
            chunk_id += 1
            chunks.append([])
            continue
        chunks[chunk_id].append(line)
    return chunks


if __name__ == "__main__":
    with open("../6.example.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        groups = chunk_lines(lines)
        assert part_one(groups) == 11
        assert part_two(groups) == 6

    with open("../6.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        groups = chunk_lines(lines)
        part_one(groups)
        part_two(groups)
