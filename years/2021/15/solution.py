#!/usr/bin/env python3
import logging
import os
import numpy as np
import networkx as nx

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger('2021:d15')
logger.setLevel(logging.DEBUG)

CWD = os.path.dirname(os.path.abspath(__file__))

def parse_grid_file(filename):
    with open(filename, 'r') as fp:
        grid = []
        for line in fp.readlines():
            grid.append([int(x) for x in list(line.strip())])
        return np.array(grid)    


def part_one(grid):
    graph = nx.grid_2d_graph(*grid.shape, create_using=nx.DiGraph)
    for _, v, d in graph.edges(data=True):
        d["weight"] = grid[v]

    start = (0, 0)
    end = (len(grid)-1, len(grid)-1)
    path = nx.shortest_path_length(graph, start, end, weight="weight")   
    logger.info(f"shortest path: {path}")
    return path


def part_two(grid):
    bigger_grid = np.block([[grid + i + j for i in range(5)] for j in range(5)])
    bigger_grid[bigger_grid > 9] -= 9
    return part_one(bigger_grid)


if __name__ == "__main__":
    grid = parse_grid_file(os.path.join(CWD, 'example.txt'))
    assert part_one(grid) == 40
    assert part_two(grid) == 315
    grid = parse_grid_file(os.path.join(CWD, 'input.txt'))
    assert part_one(grid) == 435
    assert part_two(grid) == 2842
