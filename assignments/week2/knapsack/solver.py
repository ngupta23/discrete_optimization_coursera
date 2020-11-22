#!/usr/bin/python
# -*- coding: utf-8 -*-

from typing import List, Tuple
from collections import namedtuple
from operator import attrgetter
import sys

# Need to run this from the assignments/weekX/<assignment_name> folder
sys.path.append("../../source")
from solvers.native.greedy import greedy_simple, greedy_density # type: ignore
from solvers.or_tools.knapsack import knapsack # type: ignore

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def solve_it(input_data):
    # Modify this code to run your optimization algorithm

    # parse the input
    lines = input_data.split('\n')

    firstLine = lines[0].split()
    item_count = int(firstLine[0])
    capacity = int(firstLine[1])

    items = []

    for i in range(1, item_count+1):
        line = lines[i]
        parts = line.split()
        temp_value = int(parts[0])
        temp_weight = int(parts[1])
        temp_density = temp_value/temp_weight
        items.append(Item(i-1, temp_value, temp_weight, temp_density))

    # value, taken = greedy_simple(items=items, capacity=capacity)
    # value, taken = greedy_density(items=items, capacity=capacity)
    value, taken = knapsack(items=items, capacity=capacity)
    
    # prepare the solution in the specified output format
    output_data = str(value) + ' ' + str(0) + '\n'
    output_data += ' '.join(map(str, taken))
    return output_data


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file.  Please select one from the data directory. (i.e. python solver.py ./data/ks_4_0)')

