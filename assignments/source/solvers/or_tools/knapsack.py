from typing import List, Tuple
from collections import namedtuple
from operator import attrgetter
from ortools.algorithms import pywrapknapsack_solver # type: ignore

Item = namedtuple("Item", ['index', 'value', 'weight', 'density'])

def knapsack(items: List[Item], capacity: float) -> Tuple[float, List[int]]:
    """
    Knapsack Solver using OR-Tools
    https://developers.google.com/optimization/bin/knapsack#complete-programs

    Addition Details can be found here:
    https://google.github.io/or-tools/
    http://google.github.io/or-tools/python/ortools/algorithms/pywrapknapsack_solver.html
    """ 
    values = []
    weights = []
    capacities = []
    for item in items:
        values.append(item.value)

    temp_weights = []
    for item in items:
        temp_weights.append(item.weight)
    weights.append(temp_weights)
    
    capacities = [capacity]

    # print(f"Values: {values}")
    # print(f"Weights: {weights}")

    # http://google.github.io/or-tools/python/ortools/algorithms/pywrapknapsack_solver.html
    # Dynamic Programming Solver is also available through `KNAPSACK_DYNAMIC_PROGRAMMING_SOLVER`
    solver = pywrapknapsack_solver.KnapsackSolver(
        pywrapknapsack_solver.KnapsackSolver.KNAPSACK_MULTIDIMENSION_BRANCH_AND_BOUND_SOLVER,
        'Knapsack'
    )

    # You can also set a time limit here to make sure that the solution is terminated if it takes too long
    # Use `set_time_limit()` method for this


    solver.Init(values, weights, capacities)
    computed_value = solver.Solve()
    
    taken: List[int] = []
    
    for i in range(len(values)):
        if solver.BestSolutionContains(i):
            taken.append(1)
        else:
            taken.append(0)

    # print('Taken:', taken)
    # print('Total weight:', computed_value)
    
    return computed_value, taken




