#!/usr/bin/env python3
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d8')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


def parse_display_file(filename):
    displays = []
    with open(filename, 'r') as fp:
        lines = fp.readlines()
        for line in lines:
            line = line.strip()
            signals, output = line.split('|')
            signals = signals.strip().split()
            output = output.strip().split()
            displays.append((signals, output))
    return displays


def part_one(dis):
    unique_lengths = [2, 4, 3, 7]  # digits 1, 4, 7 and 8
    total_known_outputs = 0
    for display in displays:
        for output in display[1]:
            if len(output) in unique_lengths:
                total_known_outputs += 1
    logger.info(f"{total_known_outputs} known outputs")
    return total_known_outputs


def part_two(dispays):
    known_digits_by_length = {2: '1', 3: '7', 4: '4', 7: '8'}
    total = 0
    for dis in displays:
        seven = set([signal for signal in dis[0] if len(signal) == 3][0])
        four = set([signal for signal in dis[0] if len(signal) == 4][0])
        bottom_left = set([signal for signal in dis[0] if len(signal) == 7][0])
        for letter in (four.union(seven)):
            bottom_left.discard(letter)

        output = []
        for digit in dis[1]:
            digit = set(digit)
            if len(digit) in known_digits_by_length.keys():
                output.append(known_digits_by_length[len(digit)])
            elif len(digit) == 6:
                if four < digit:
                    output.append('9')
                elif seven < digit:
                    output.append('0')
                else:
                    output.append('6')
            else:
                if seven < digit:
                    output.append('3')
                elif bottom_left < digit:
                    output.append('2')
                else:
                    output.append('5')

        output = int(''.join(output))
        total = total + output
    logger.info(f"total: {total}")
    return total


if __name__ == "__main__":
    logger.info('example.txt')
    displays = parse_display_file(os.path.join(CWD, 'example.txt'))
    assert part_one(displays) == 26
    assert part_two(displays) == 61229
    logger.info('input.txt')
    displays = parse_display_file(os.path.join(CWD, 'input.txt'))
    assert part_one(displays) == 294
    assert part_two(displays) == 973292
