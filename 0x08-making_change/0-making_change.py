#!/usr/bin/python3
"""
determines least coins to return change
"""


def makeChange(coins, total):
    """
    returns the least change
    """
    if total <= 0:
        return 0
    # Create array to hold minimum number of coins required to reach each value
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            # Update minimum number of coins required for each value
            min_coins[i] = min(min_coins[i], min_coins[i - coin] + 1)

    # Return minimum number of coins required to reach total value
    return min_coins[total] if min_coins[total] != float('inf') else -1
