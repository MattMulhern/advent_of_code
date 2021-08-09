#!/usr/bin/python3


def update_pos(i, char, santa_pos_x, santa_pos_y, rob_pos_x, rob_pos_y):
    if (i % 2 == 0):  # even == santa
        if char == '^':
            santa_pos_y += 1
            pos_str = "{0}x{1}".format(santa_pos_x, santa_pos_y)
        if char == 'v':
            santa_pos_y -= 1
            pos_str = "{0}x{1}".format(santa_pos_x, santa_pos_y)
        if char == '>':
            santa_pos_x += 1
            pos_str = "{0}x{1}".format(santa_pos_x, santa_pos_y)
        if char == '<':
            santa_pos_x -= 1
            pos_str = "{0}x{1}".format(santa_pos_x, santa_pos_y)
    else:  # odd == rob
        if char == '^':
            rob_pos_y += 1
            pos_str = "{0}x{1}".format(rob_pos_x, rob_pos_y)
        if char == 'v':
            rob_pos_y -= 1
            pos_str = "{0}x{1}".format(rob_pos_x, rob_pos_y)
        if char == '>':
            rob_pos_x += 1
            pos_str = "{0}x{1}".format(rob_pos_x, rob_pos_y)
        if char == '<':
            rob_pos_x -= 1
            pos_str = "{0}x{1}".format(rob_pos_x, rob_pos_y)
    return santa_pos_x, santa_pos_y, rob_pos_x, rob_pos_y, pos_str


def walk_santa_and_robot(input):
    """
    TODO: should use globals here instead of passing positions back and forth.
    """
    houses = {}
    houses["0x0"] = 2
    santa_pos_x = 0
    santa_pos_y = 0
    rob_pos_x = 0
    rob_pos_y = 0
    for line in input:
        for i, char in enumerate(line.strip()):
            santa_pos_x, santa_pos_y, rob_pos_x, rob_pos_y, pos_str = \
                update_pos(i, char, santa_pos_x, santa_pos_y, rob_pos_x, rob_pos_y)

            if pos_str not in houses.keys():
                houses[pos_str] = 0
            houses[pos_str] += 1

        total = 0
        for pos in houses.keys():
            if houses[pos] > 0:
                total += 1
        print("With Santa and RoboSanta there are {0} houses with one or more presents".format(total))


def walk_santa(input):
    """
    TODO: refactor to use update_pos(or derivative) above
    """
    for line in input:
        houses = {}
        houses["0x0"] = 1
        pos_x = 0
        pos_y = 0
        for char in line.strip():
            if char == '^':
                pos_y += 1
                pos_str = "{0}x{1}".format(pos_x, pos_y)
                if pos_str not in houses.keys():
                    houses[pos_str] = 0
                houses[pos_str] += 1
            elif char == 'v':
                pos_y -= 1
                pos_str = "{0}x{1}".format(pos_x, pos_y)
                if pos_str not in houses.keys():
                    houses[pos_str] = 0
                houses[pos_str] += 1
            elif char == '>':
                pos_x  += 1
                pos_str = "{0}x{1}".format(pos_x, pos_y)
                if pos_str not in houses.keys():
                    houses[pos_str] = 0
                houses[pos_str] += 1
            elif char == '<':
                pos_x  -= 1
                pos_str = "{0}x{1}".format(pos_x, pos_y)
                if pos_str not in houses.keys():
                    houses[pos_str] = 0
                houses[pos_str] += 1
            else:
                print("{0} not recognised!".format(char))

        total = 0
        for pos in houses.keys():
            if houses[pos] > 0:
                total += 1
        print("With just Santa there are {0} houses with one or more presents".format(total))

if __name__ == '__main__':
    input = open('./input.txt', 'r').readlines()
    walk_santa(input)
    walk_santa_and_robot(input)
