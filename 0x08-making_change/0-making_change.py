#!/usr/bin/python3
"""
determines least coins toreturn change
"""
def change_sub(coins, total, solutions):
    """
    helper function to deterine least coins
    """
    if total < 0:
        return -1
    if total == 0:
        return 0
    if solutions[total -1] != 0:
        return solutions[total - 1]

    optimal_solution = float('inf')

    for coin in coins:
        best_solution_for_coin = change_sub(coins, total - coin, solutions)
        if 0<= best_solution_for_coin < optimal_solution:
            optimal_solution = best_solution_for_coin + 1

    if optimal_solution == float('inf'):
        solutions[total -1] = -1
    else:
        solutions[total - 1] = optimal_solution

    return solutions[total - 1]

def makeChange(coins, total):
    """
    returns the least change
    """
    if total < 1:
        return 0
    return change_sub(coins, total, [0] * total)
