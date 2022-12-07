#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.DEBUG)
CWD = os.path.dirname(os.path.abspath(__file__))


class FilePath:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {}


def parse_file(filename):
    with open(filename, "r") as fp:
        return fp.readlines()


def build_tree(raw):
    root = FilePath("/", 0, None)
    cwd = root
    for line in raw:
        line = line.split()
        if line[0] == "$":
            if line[1] == "cd":
                if line[2] == "/":
                    cwd = root
                elif line[2] == "..":
                    cwd = cwd.parent
                else:
                    cwd = cwd.children[line[2]]
        else:
            name = line[1]
            if line[0] == "dir":
                size = 0
            else:
                size = int(line[0])
            new_path = FilePath(name, size, cwd)
            cwd.children[new_path.name] = new_path
    return root


def calculate_sizes(directory):
    directory.total_size = 0
    for child in directory.children.values():
        directory.total_size += calculate_sizes(child) if child.children else child.size
    return directory.total_size


def find_sizes_under_threshold(directory, sizes, threshold=100000):
    for child in directory.children.values():
        if child.children:
            find_sizes_under_threshold(child, sizes, threshold)
    if directory.total_size <= threshold:
        sizes.append(directory.total_size)


def find_suitable_deletion_sizes(directory, suitable_sizes, space_needed):
    for child in directory.children.values():
        if child.children:
            find_suitable_deletion_sizes(child, suitable_sizes, space_needed)
    if directory.total_size >= space_needed:
        suitable_sizes.append(directory.total_size)


def part_one(raw):
    logger = logging.getLogger("2022:d7:p1")
    root = build_tree(raw)
    calculate_sizes(root)
    sizes = []
    threshold = 100000
    find_sizes_under_threshold(root, sizes, threshold)
    total = sum(sizes)
    logger.info(f"the sum of dir sizes under {threshold} is {total}")
    return total


def part_two(raw):
    logger = logging.getLogger("2022:d7:p2")
    root = build_tree(raw)
    calculate_sizes(root)
    hd_size = 70000000
    min_space_needed = 30000000
    space_needed = min_space_needed - hd_size + root.total_size
    logger.info(f"space_needed:{space_needed}")
    sizes = []
    find_suitable_deletion_sizes(root, sizes, space_needed)
    target = min(sizes)
    logger.info(f"We should delete the dir with size {target}")
    return target


if __name__ == "__main__":
    my_input = parse_file(os.path.join(CWD, "example.txt"))
    assert part_one(my_input) == 95437
    assert part_two(my_input) == 24933642

    my_input = parse_file(os.path.join(CWD, "input.txt"))
    assert part_one(my_input) == 1350966
    assert part_two(my_input) == 6296435
