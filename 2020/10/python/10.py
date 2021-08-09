#!/usr/bin/env python
# used for part 2
adapter_uses = {}


def part_one(nums):
    print("*** PART 1 ***")

    max_joltage = nums[-1] + 3
    nums.append(max_joltage)

    cur_joltage = 0
    total_1j_diffs = 0
    total_3j_diffs = 0
    for adapter in nums:
        jdiff = adapter - cur_joltage
        if jdiff == 1:
            total_1j_diffs += 1
        elif jdiff == 3:
            total_3j_diffs += 1
        else:
            print(f"{adapter} - {cur_joltage} = {jdiff}")  # I'm not yet sure if this should ever be hit.
        cur_joltage = adapter
    print(f"Using all adapters, there are {total_1j_diffs} 1J diffs and {total_3j_diffs} 3J diffs")
    return total_1j_diffs, total_3j_diffs


def part_two(nums):
    adapter_uses.clear()
    print("*** PART 2 ***")
    nums.append(nums[-1] + 3)
    nums.insert(0, 0)
    num_paths = walk(0, nums, adapter_uses)
    print(f"There are {num_paths} possible paths from 0 to {nums[-1]}")
    return num_paths


def walk(index, nums, adapter_uses):
    result = 0
    possible_indexes = []
    if index not in adapter_uses:
        for i in range(index + 1, len(nums)):
            if i < len(nums):
                if nums[i] - nums[index] in (1, 2, 3):
                    possible_indexes.append(i)
            else:
                break
        if possible_indexes:
            for num in possible_indexes:
                result += walk(num, nums, adapter_uses)
                adapter_uses[index] = result
        else:
            return 1
    return adapter_uses[index]


if __name__ == "__main__":
    print("*** EXAMPLE ***")
    with open("../10.example.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        assert part_one(sorted(nums)) == (7, 5)
        assert part_two(sorted(nums)) == 8

    with open("../10.example2.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        assert part_one(sorted(nums)) == (22, 10)
        assert part_two(sorted(nums)) == 19208

    with open("../10.example.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        assert part_one(sorted(nums)) == (7, 5)
        assert part_two(sorted(nums)) == 8

    print("\n*** MY INPUT ***")
    with open("../10.input.txt", "r") as fp:
        nums = [int(x.strip()) for x in fp.readlines()]
        diffs = part_one(sorted(nums))
        assert diffs == (64, 37)
        print(f"{diffs[0]} * {diffs[1]} = {diffs[0] * diffs[1]}")
        assert part_two(sorted(nums)) == 1727094849536
