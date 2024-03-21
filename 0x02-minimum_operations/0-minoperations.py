#!/usr/bin/python3
"""
Minimum operations funtion

In a text file, there is a single character H.
Your text editor can execute only two operations in this file:
Copy All and Paste. Given a number n, write a method that
calculates the fewest number of operations needed to result
in exactly n H characters in the file.
"""
import math


def factors(num):
    """
    Gets the factors of number
    """
    mylist = []
    while num % 2 == 0:
        mylist.append(2)
        num = num / 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            mylist.append(i)
            num = num / i
    if num > 2:
        mylist.append(num)
    return mylist


def minOperations(n):
    """
    determines minimum number of operations to result exactly n H characters
    """
    if not isinstance(n, int) or n < 2:
        return 0
    else:
        numOperations = sum(factors(n))
        return int(numOperations)
