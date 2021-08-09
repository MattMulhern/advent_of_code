#!/usr/bin/env python

def is_valid(num, preamble):
    # print(f"checking if {num} is valid")
    for pnuma in preamble:
        for pnumb in preamble:
            if pnuma == pnumb:
                continue
            if pnuma + pnumb == num:
                return True
    # print(f"{num} is invalid!")
    return False


def find_frist_invalid_num(nums, prelen=25):
    for idx, num in enumerate(nums):
        if idx <= prelen:
            continue  # skip the initial preamble
        preamble = nums[idx-prelen:idx]
        if not is_valid(num, preamble):
            return num, idx


def part_one(nums, prelen=25):
    print("*** PART 1 ***")
    invalid_num, idx = find_frist_invalid_num(nums, prelen=prelen)
    print(f"The first invalid number in the input is {invalid_num} at index {idx}")
    return invalid_num


def part_two(nums, prelen=25):
    print("*** PART 2 ***")
    invalid_num, invalid_idx = find_frist_invalid_num(nums, prelen=prelen)
    range_lower_idx, range_upper_idx = find_first_range(invalid_num, invalid_idx, nums)
    summation = sum_max_and_min(nums, range_lower_idx, range_upper_idx)
    print(f"The sum of the highest and lowest value in the first range equalling the first invalid number is {summation}")
    return summation


def find_first_range(invalid_num, invalid_idx, nums):
    for lidx, num in enumerate(nums[:invalid_idx]):
        for uidx, num in enumerate(nums[:invalid_idx]):
            if lidx == uidx:
                continue
            # print(f"sum({nums[lidx:uidx+1]}) = {sum(nums[lidx:uidx+1])}")
            if sum(nums[lidx:uidx+1]) == nums[invalid_idx]:
                return lidx, uidx+1


def sum_max_and_min(nums, upper_idx, lower_idx):
    return min(nums[upper_idx:lower_idx]) + max(nums[upper_idx:lower_idx])


if __name__ == "__main__":
    print("*** EXAMPLE ***")
    with open("../9.example.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        assert part_one(nums, prelen=5) == 127
        assert part_two(nums, prelen=5) == 62

    print("\n*** MY INPUT ***")
    with open("../9.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        assert part_one(nums, prelen=25) == 104054607
        assert part_two(nums, prelen=25) == 13935797
