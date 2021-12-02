#!/usr/bin/env python
def part_one(rows):
    print("*** PART 1 ***")
    num_seatings = 0
    while True:
        newrows = seat(rows)
        if newrows == rows:
            break
        num_seatings += 1
        rows = newrows

    occupied = count_occupied(rows)
    print(f"It took {num_seatings} seatings to reach a stable pattern, at which {occupied} seats were occupied!")

    return occupied


def count_occupied(rows):
    total = 0
    for row in rows:
        total += row.count('#')
    return total


def get_surrounding_seats(rows, r, c):
    surrounding_seats = []
    for pos in [(r-1, c-1), (r-1, c), (r-1, c+1), (r, c+1), (r+1, c+1), (r+1, c), (r+1, c-1), (r, c-1)]:

        if (pos[0] < 0) or (pos[0] >= len(rows)) or (pos[1] < 0) or (pos[1] >= len(rows[0])):
            surrounding_seats.append('.')
        else:
            surrounding_seats.append(rows[pos[0]][pos[1]])
    return surrounding_seats


def seat(rows):
    newrows = []
    for x, row in enumerate(rows):
        newrows.append([])
        for y, space in enumerate(row):
            if space == '.':
                newrows[x].append('.')
                continue   # floor spaces don't change
            surrounding_seats = get_surrounding_seats(rows, x, y)
            if (space == 'L') and (surrounding_seats.count('#') == 0):
                newrows[x].append('#')
            elif (space == '#') and (surrounding_seats.count('#') >= 4):
                newrows[x].append('L')
            else:
                newrows[x].append(space)

    return newrows


def print_rows(rows):
    for row in rows:
        print(f"{''.join(row)}, [{len(row)}]")


def print_three_rowsets(itera, iterb, iterc):
    print()
    for i, row in enumerate(itera):
        print(f"{''.join(itera[i])} -> {''.join(iterb[i])} ?? {''.join(iterc[i])}")


def seat_visible(rows):
    newrows = []
    for x, row in enumerate(rows):
        newrows.append([])
        for y, space in enumerate(row):
            if space == '.':
                newrows[x].append('.')
                continue   # floor spaces don't change
            visibles = get_visible_seats(rows, x, y)
            num_visibles_occupied = count_surrounding_occupied(visibles)
            if (space == 'L') and (num_visibles_occupied == 0):
                newrows[x].append('#')
            elif (space == '#') and (num_visibles_occupied >= 5):
                newrows[x].append('L')
            else:
                newrows[x].append(space)

    return newrows


def get_visible_seats(pattern, row, col):
    n_x, n_y, n_val = get_north_visible(pattern, row, col)
    s_x, s_y, s_val = get_south_visible(pattern, row, col)
    e_x, e_y, e_val = get_east_visible(pattern, row, col)
    w_x, w_y, w_val = get_west_visible(pattern, row, col)
    ne_x, ne_y, ne_val = get_north_east_visible(pattern, row, col)
    se_x, se_y, se_val = get_south_east_visible(pattern, row, col)
    nw_x, nw_y, nw_val = get_north_west_visible(pattern, row, col)
    sw_x, sw_y, sw_val = get_south_west_visible(pattern, row, col)

    visibles = {'n': [n_x, n_y, n_val],
                's': [s_x, s_y, s_val],
                'e': [e_x, e_y, e_val],
                'w': [w_x, w_y, w_val],
                'ne': [ne_x, ne_y, ne_val],
                'se': [se_x, se_y, se_val],
                'nw': [nw_x, nw_y, nw_val],
                'sw': [sw_x, sw_y, sw_val]}
    return visibles


def get_north_east_visible(pattern, row, col):
    # print(f"checking north-east FROM [{row}][{col}]")
    x = row-1
    y = col+1
    if (row == 0) or (col == len(pattern[0])-1):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{y}]", end='')
        if (x == 0) or (y == len(pattern[0])-1):
            # print(f"{pattern[x][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][y] != '.':
            # print(f"{pattern[x][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][y]}")
            x -= 1
            y += 1


def get_north_west_visible(pattern, row, col):
    # print(f"checking north-west FROM [{row}][{col}]")
    x = row-1
    y = col-1
    if (row == 0) or (col == 0):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{y}]", end='')
        if (x == 0) or (y == 0):
            # print(f"{pattern[x][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][y] != '.':
            # print(f"{pattern[x][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][y]}")
            x -= 1
            y -= 1


def get_south_west_visible(pattern, row, col):
    # print(f"checking south-west FROM [{row}][{col}]")
    x = row+1
    y = col-1
    if (row == len(pattern)-1) or (col == 0):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{y}]", end='')
        if (x == len(pattern)-1) or (y == 0):
            # print(f"{pattern[x][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][y] != '.':
            # print(f"{pattern[x][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][y]}")
            x += 1
            y -= 1


def get_south_east_visible(pattern, row, col):
    # print(f"checking south-east FROM [{row}][{col}]")
    x = row+1
    y = col+1
    if (row == len(pattern)-1) or (col == len(pattern[0])-1):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{y}]", end='')
        if (x == len(pattern)-1) or (y == len(pattern[0])-1):
            # print(f"{pattern[x][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][y] != '.':
            # print(f"{pattern[x][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][y]}")
            x += 1
            y += 1


def get_north_visible(pattern, row, col):
    # print(f"checking FROM [{row}][{col}]")
    x = row-1
    y = col
    if (row == 0):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{col}]", end='')
        if x == 0:
            # print(f"{pattern[x][col]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][col] != '.':
            # print(f"{pattern[x][col]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][col]}")
            x -= 1


def get_south_visible(pattern, row, col):
    x = row+1
    y = col
    # print(f"checking FROM [{row}][{col}]")
    if (row == len(pattern)-1):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{x}][{col}]", end='')
        if x == (len(pattern)-1):
            # print(f"{pattern[x][col]} END!")
            return x, y, pattern[x][y]
        elif pattern[x][col] != '.':
            # print(f"{pattern[x][col]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[x][col]}")
            x += 1


def get_east_visible(pattern, row, col):
    x = row
    y = col+1
    # print(f"checking east FROM [{row}][{col}]")
    if (col == len(pattern[0])-1):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{row}][{y}]", end='')
        if y == len(pattern[0])-1:
            # print(f"{pattern[row][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[row][y] != '.':
            # print(f"{pattern[row][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[row][y]}")
            y += 1


def get_west_visible(pattern, row, col):
    x = row
    y = col-1
    # print(f"checking FROM [{row}][{col}]")
    if (col == 0):
        return None, None, '.'  # already on edge!
    while True:
        # print(f"checking [{row}][{y}]", end='')
        if y == 0:
            # print(f"{pattern[row][y]} END!")
            return x, y, pattern[x][y]
        elif pattern[row][y] != '.':
            # print(f"{pattern[row][y]} HAH!")
            return x, y, pattern[x][y]
        else:
            # print(f"{pattern[row][y]}")
            y -= 1


def count_surrounding_occupied(visibles):
    if len(visibles) != 8:
        raise ValueError(f"bad visibles! {visibles}")

    total = 0
    for direction, seat in visibles.items():
        if seat[2] == '#':
            total += 1
    return total


def part_two(rows):
    print("*** PART 2 ***")
    num_seatings = 0
    while True:
        newrows = seat_visible(rows)
        if newrows == rows:
            break
        num_seatings += 1
        rows = newrows

    occupied = count_occupied(rows)
    print(f"It took {num_seatings} seatings to reach a stable pattern, at which {occupied} seats were occupied!")
    return occupied


def test_example_input():
    print("*** EXAMPLE ***")
    with open("../11.example.input.txt", "r") as fp:
        lines = [list(x.strip()) for x in fp.readlines()]
        iterations = [[]]
        i = 0
        for line in lines:
            if len(line) == 0:
                iterations.append([])
                i += 1
                continue
            iterations[i].append(line)
        assert seat(iterations[0]) == iterations[1]
        assert seat(iterations[1]) == iterations[2]
        assert seat(iterations[2]) == iterations[3]
        assert seat(iterations[3]) == iterations[4]
        assert part_one(iterations[0]) == 37

    with open("../11.example.input.part2.txt", "r") as fp:
        lines = [list(x.strip()) for x in fp.readlines()]
        patterns = [[]]
        i = 0
        for line in lines:
            if len(line) == 0:
                patterns.append([])
                i += 1
                continue
            patterns[i].append(line)

        assert count_surrounding_occupied(get_visible_seats(patterns[0], 4, 3)) == 8
        assert count_surrounding_occupied(get_visible_seats(patterns[1], 1, 1)) == 0
        assert count_surrounding_occupied(get_visible_seats(patterns[1], 1, 3)) == 1
        assert count_surrounding_occupied(get_visible_seats(patterns[2], 3, 3)) == 0

        assert seat_visible(patterns[3]) == patterns[4]
        assert seat_visible(patterns[4]) == patterns[5]
        assert seat_visible(patterns[5]) == patterns[6]
        assert seat_visible(patterns[6]) == patterns[7]
        assert seat_visible(patterns[7]) == patterns[8]
        assert seat_visible(patterns[8]) == patterns[9]
        assert seat_visible(patterns[9]) == patterns[9]
        assert part_two(patterns[3]) == 26


def test_my_input():
    print("*** MY INPUT ***")
    with open("../11.input.txt", "r") as fp:
        lines = [list(x.strip()) for x in fp.readlines()]
        assert part_one(lines) == 2344
        assert part_two(lines) == 2076


if __name__ == "__main__":
    test_example_input()
    test_my_input()
