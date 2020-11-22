from typing import List, Tuple
from collections import namedtuple
from operator import attrgetter
Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def greedy_density(items: List[Item], capacity: float) -> Tuple[float, List[int]]:
    """
    A greedy algorithm for filling the knapsack based on
    the value density until the capacity is exhausted
    """ 
    value = 0
    weight = 0
    taken: List[int] = [0]*len(items)

    for item in sorted(items, key=attrgetter('density'), reverse=True):
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken

def greedy_simple(items: List[Item], capacity: float) -> Tuple[float, List[int]]:
    """
    A trivial algorithm for filling the knapsack
    It takes items in-order until the knapsack is full
    """ 
    value = 0
    weight = 0
    taken: List[int] = [0]*len(items)

    for item in items:
        if weight + item.weight <= capacity:
            taken[item.index] = 1
            value += item.value
            weight += item.weight

    return value, taken