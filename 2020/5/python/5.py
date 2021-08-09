#!/usr/bin/env python
def part_one(lines):
    """ my correct answer was 922 """
    print("*** PART 1 ***")
    ids = []
    for bpass in lines:
        ids.append(find_id(bpass))
    print(f"The highest seat id is {sorted(ids)[-1]}")


def part_two(lines):
    """ my correct answer was  747"""
    print("*** PART 2 ***")
    sids = []
    for bpass in lines:
        sids.append(find_id(bpass))
    # we're looking for a sid id missing but with sid+1 and sid-1 present.
    # easier to find the sid to the left of that (i.e. sid with sid+1 missing but sid-2 present)
    empty_sids = [sid+1 for sid in sids if sid+1 not in sids and sid+2 in sids]

    assert len(empty_sids) == 1
    print(f"My seat id is {empty_sids[0]}")


def drop_upper_half(seats):
    amount_to_drop = int(len(seats)/2)
    return seats[amount_to_drop:]


def drop_lower_half(seats):
    amount_to_drop = int(len(seats)/2)
    return seats[:amount_to_drop]


def find_row(bpass):
    seats = list(range(128))
    for char in bpass[0:7]:
        if char == 'B':
            seats = drop_upper_half(seats)
        elif char == 'F':
            seats = drop_lower_half(seats)
        else:
            raise ValueError(f"unexpected char {char}")

    assert len(seats) == 1  # THERE CAN ONLY BE ONE!
    return seats[0]


def find_col(bpass):
    seats = list(range(8))
    for char in bpass[-3:]:
        if char == 'R':
            seats = drop_upper_half(seats)
        elif char == 'L':
            seats = drop_lower_half(seats)
        else:
            raise ValueError(f"unexpected char {char}")

    assert len(seats) == 1  # THERE CAN ONLY BE ONE!
    return seats[0]


def find_id(bpass):
    row = find_row(bpass)
    col = find_col(bpass)
    return (row * 8) + col


if __name__ == "__main__":
    test_passes = ["BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
    assert (find_row(test_passes[0]) == 70)
    assert (find_row(test_passes[1]) == 14)
    assert (find_row(test_passes[2]) == 102)

    assert (find_col(test_passes[0]) == 7)
    assert (find_col(test_passes[1]) == 7)
    assert (find_col(test_passes[2]) == 4)

    assert (find_id(test_passes[0]) == 567)
    assert (find_id(test_passes[1]) == 119)
    assert (find_id(test_passes[2]) == 820)

    with open("../5.input.txt", "r") as fp:
        lines = [x.strip() for x in fp.readlines()]
        part_one(lines)
        part_two(lines)
