#!/usr/bin/python3
def find_floor(line):
    floor = 0
    for char in line.strip():
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print("error on char!")
    print ("Final Floor:{0}".format(floor))


def find_floors(line):
    floor = 0
    floors = {}
    for i, char in enumerate(line.strip(), start=1):
        if char == '(':
            floor += 1
        elif char == ')':
            floor -= 1
        else:
            print("error on char!")
        if floor not in floors.keys():
            floors[floor] = i
    print("The Position of the char first bringing santa to the -1 basement is ",
          floors[-1])

if __name__ == '__main__':
    input = open('./input.txt', 'r').readlines()

    for line in input:
        find_floor(line)

    for line in input:
        find_floors(line)
