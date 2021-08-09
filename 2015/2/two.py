#!/usr/bin/python3
import os


def find_required_paper(filename, input_file):
    total_paper = 0
    for line in input_file:
        # sort and store array of dimensions
        dimensions = []
        dimension_strings = line.strip().split('x')
        for dim in dimension_strings:
            dimensions.append(int(dim))
        dimensions.sort()

        # work out each square seperatly to compare
        s1 = (dimensions[0] * dimensions[1])
        s2 = (dimensions[1] * dimensions[2])
        s3 = (dimensions[2] * dimensions[0])

        # total SQ of box + smallest side spair "extra"
        total_paper += (2 * s1) + (2 * s2) + (2 * s3) + min([s1, s2, s3])
    print ("{0}: Required total paper = {1}".format(filename, total_paper))


def find_required_ribbon(filename, input_file):
    total_ribbon = 0
    for line in input_file:
        # sort and store array of dimensions
        dimensions = []
        dimension_strings = line.strip().split('x')
        for dim in dimension_strings:
            dimensions.append(int(dim))
        dimensions.sort()

        wrappping_ribbon  = (2 * dimensions[0]) + (2 * dimensions[1])
        bow_ribbon        = dimensions[0] * dimensions[1] * dimensions[2]

        total_ribbon += (wrappping_ribbon + bow_ribbon)
    print ("{0}: Required total ribbon = {1}".format(filename, total_ribbon))


if __name__ == '__main__':
    for input_file in os.listdir('./inputs'):
        filename = './inputs/{0}'.format(input_file)
        input = open(filename, 'r').readlines()

        find_required_paper(filename, input)
        find_required_ribbon(filename, input)
