#!/usr/bin/env python3

import math
import sys
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d16')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))


class Packet:
    def __init__(self, version, type, value, packets=[]):
        self.version = version
        self.type = type
        self.value = value
        self.packets = packets

    @staticmethod
    def from_hex(bits):
        idx = 0

        version = int(bits[idx:idx + 3], 2)
        ptype = int(bits[idx + 3:idx + 6], 2)

        idx += 6

        if ptype == 4:
            value = ""
            while idx < len(bits):
                next_digit = int(bits[idx], 2)
                value += bits[idx + 1:idx + 5]
                idx += 5
                if next_digit == 0:
                    break
            return Packet(version, ptype, int(value, 2)), idx

        packets = []
        length_type = int(bits[idx], 2)
        idx += 1

        if length_type == 0:
            length = int(bits[idx:idx + 15], 2)
            idx += 15
            while length > 0:
                packet, bits_read = Packet.from_hex(bits[idx:idx + length])
                idx += bits_read
                length -= bits_read
                packets.append(packet)

        else:
            count = int(bits[idx:idx + 11], 2)
            idx += 11
            while count > 0:
                packet, bits_read = Packet.from_hex(bits[idx:])
                idx += bits_read
                count -= 1
                packets.append(packet)

        return Packet(version, ptype, 0, packets), idx

    def sum_version(self) -> int:
        version = 0
        packets = [self]
        while packets:
            packet = packets.pop()
            version += packet.version
            packets.extend(packet.packets)
        return version

    def result(self) -> int:
        if self.type == 4:
            return self.value

        results = [p.result() for p in self.packets]

        if self.type == 0:
            return sum(results)
        elif self.type == 1:
            return math.prod(results)
        elif self.type == 2:
            return min(results)
        elif self.type == 3:
            return max(results)
        elif self.type == 5:
            return int(results[0] > results[1])
        elif self.type == 6:
            return int(results[0] < results[1])
        elif self.type == 7:
            return int(results[0] == results[1])


def hex_to_bin(hex_in):
    hex_to_bin_dict = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'}
    bin_vals = []
    for hex_char in hex_in:
        bin_vals.append(hex_to_bin_dict[hex_char])
    return ''.join(bin_vals)


def test_structures():
    assert hex_to_bin('D2FE28') == '110100101111111000101000'
    # literal packet
    packet_bits = hex_to_bin('D2FE28')
    packet, _ = Packet.from_hex(packet_bits)
    assert packet.type == 4
    assert packet.version == 6
    assert len(packet.packets) == 0
    assert packet.value == 2021

    # type 0 operator
    packet_bits = hex_to_bin('38006F45291200')
    packet, _ = Packet.from_hex(packet_bits)
    assert packet.type == 6
    assert packet.version == 1
    assert len(packet.packets) == 2
    assert packet.packets[0].value == 10
    assert packet.packets[1].value == 20

    # type 1 operator
    packet_bits = hex_to_bin('EE00D40C823060')
    packet, _ = Packet.from_hex(packet_bits)
    assert packet.type == 3
    assert packet.version == 7
    assert len(packet.packets) == 3
    assert packet.packets[0].value == 1
    assert packet.packets[1].value == 2
    assert packet.packets[2].value == 3

    logger.info("all structure tests passed!")


def test_results():
    packet, _ = Packet.from_hex(hex_to_bin('EE00D40C823060'))
    assert packet.result() == 3
    packet, _ = Packet.from_hex(hex_to_bin('04005AC33890'))
    assert packet.result() == 54
    packet, _ = Packet.from_hex(hex_to_bin('880086C3E88112'))
    assert packet.result() == 7
    packet, _ = Packet.from_hex(hex_to_bin('CE00C43D881120'))
    assert packet.result() == 9
    packet, _ = Packet.from_hex(hex_to_bin('D8005AC2A8F0'))
    assert packet.result() == 1
    packet, _ = Packet.from_hex(hex_to_bin('F600BC2D8F'))
    assert packet.result() == 0
    packet, _ = Packet.from_hex(hex_to_bin('9C005AC2F8F0'))
    assert packet.result() == 0
    packet, _ = Packet.from_hex(hex_to_bin('9C0141080250320F1802104A08'))
    assert packet.result() == 1

    logger.info("all result tests passed!")


if __name__ == '__main__':
    test_structures()
    test_results()

    packet_hex = open(os.path.join(CWD, 'input.txt')).read().strip()
    packet_bits = hex_to_bin(packet_hex)
    packet, _ = Packet.from_hex(packet_bits)

    print(f'Total of all packet versions {packet.sum_version()}')
    print(f'Transmission value: {packet.result()}')

    sys.exit(0)
