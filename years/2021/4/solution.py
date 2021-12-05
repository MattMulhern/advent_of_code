#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d4')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def sum_values(card):
    total = 0
    for row in card:
        for val in row:
            if val != 'x':
                total += int(val)
    return total


def check_winning(card):
    # check for winning row
    for row in card:
        if (row[0] == 'x') and len(set(row)) == 1:
            return True

    # check for winning column
    for col_index, _ in enumerate(card[0]):
        column = [row[col_index] for row in card]
        if (column[0] == 'x') and len(set(column)) == 1:
            return True
    return False


def update_card(card, number):
    """ update card marking number matching with X.    """
    new_card = []
    for line in card:
        new_line = []
        for value in line:
            if value == number:
                new_line.append('x')
            else:
                new_line.append(value)
        new_card.append(new_line)
    return new_card


def parse_bingo_file(filename):
    with open(filename, 'r') as fp:
        logger.info(f"parsing {filename}")
        lines = [x.strip() for x in fp.readlines()]
        numbers = lines[0].split(',')
        cards = []
        index = -1
        for line in lines[1:]:
            if line == '':
                index += 1
                cards.append([])
            else:
                cards[index].append(line.split())
        return numbers, cards


def part_one(numbers, cards):
    for number in numbers:
        for card_index, _ in enumerate(cards):
            cards[card_index] = update_card(cards[card_index], number)
            if check_winning(cards[card_index]):
                unmarked_sum = sum_values(cards[card_index])
                product = unmarked_sum * int(number)
                logger.info(f"{unmarked_sum} * {number} = {product}")
                return product


def part_two(numbers, cards):
    winning_cards = []
    for number in numbers:
        for card_index, _ in enumerate(cards):
            if card_index in winning_cards:
                continue
            cards[card_index] = update_card(cards[card_index], number)
            if check_winning(cards[card_index]):
                winning_cards.append(card_index)
                if len(winning_cards) == len(cards):
                    logger.debug(winning_cards)
                    unmarked_sum = sum_values(cards[winning_cards[-1]])
                    product = unmarked_sum * int(number)
                    logger.info(f"{unmarked_sum} * {number} = {product}")
                    return product


if __name__ == "__main__":
    logger.info('example.txt')
    numbers, cards = parse_bingo_file(os.path.join(CWD, 'example.txt'))
    assert part_one(numbers, cards) == 4512
    assert part_two(numbers, cards) == 1924
    logger.info('input.txt')
    numbers, cards = parse_bingo_file(os.path.join(CWD, 'input.txt'))
    assert part_one(numbers, cards) == 87456
    assert part_two(numbers, cards) == 15561
