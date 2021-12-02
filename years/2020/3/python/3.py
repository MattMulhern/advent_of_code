#!/usr/bin/env python

    # valid_count = 0
    # for line in lines:
    #     splitline = line.strip().split()
    #     char = splitline[1].strip(":")
    #     ranges = [int(x) for x in splitline[0].split("-")]
    #     password = splitline[-1]
    #     if (password.count(char) >= ranges[0]) and (password.count(char) <= ranges[1]):
    #         valid_count += 1
    # print(f"There are {valid_count} valid passwords")



def load_treemap(lines):
    treemap = []
    for line in lines:
        # replace chars with '_' and 'T' (for easier reading only) and split into list
        treemap.append(list(line.strip().replace('#', 'T').replace('.', '_')))
    return treemap


def tobbagan(x, y, treemap, xdiff=3, ydiff=1):
    width = len(treemap[0])
    height = len(treemap)
    collisions = 0

    new_x = x + xdiff
    new_y = y + ydiff

    if new_x >= width:
        # print(f"wrapping xpos from {new_x} to {new_x - width}")
        new_x -= width
    if treemap[new_y][new_x] == 'T':
        collisions = 1

    return new_x, new_y, collisions

def part_one(treemap):
    """ my correct answer was 'the product of all collisions is 9533698720' """
    print("*** PART 1 ***")
    x = 0
    y = 0
    total_collisions = 0
    while True:
        # print(f"moving from line {y} to line {y+1} of {len(treemap)}")
        x, y, collided = tobbagan(x, y, treemap)
        total_collisions += collided
        if y == len(treemap)-1:
            break
    print (f"ended up in ({x}, {y}) after landing on {total_collisions} trees.")


def part_two(lines):
    """ my correct answer was  """
    print("*** PART 2 ***")
    routes = ["Right 1, down 1.",
              "Right 3, down 1.",
              "Right 5, down 1.",
              "Right 7, down 1.",
              "Right 1, down 2."]
    route_collisions = {}
    for route in routes:
        x=0
        y=0
        total_collisions = 0

        splitline = route.strip('.').replace(',', '').split()
        across, down = int(splitline[1]), int(splitline[3])

        while True:
            # print(f"moving from line {y} to line {y+1} of {len(treemap)}")
            x, y, collided = tobbagan(x, y, treemap, xdiff=across, ydiff=down)
            total_collisions += collided
            if y >= len(treemap)-1:
                break
        route_collisions[route] = total_collisions
    product = 1
    for route, collisions in route_collisions.items():
        print(f"{route} leads to {collisions} trees.")
        product *= collisions
    print(f"the product of all collisions is {product}")


if __name__ == "__main__":
    # with open("../3.example.input.txt", "r") as fp:
    with open("../3.input.txt", "r") as fp:
        lines = fp.readlines()
        treemap = load_treemap(lines)
        part_one(treemap)
        part_two(treemap)
