#!/usr/bin/python3
"""
N queens” solution finder.
This is a classic problem in computer science
and mathematics, known for its application of the backtracking algorithm
to place N non-attacking queens on an N×N chessboard.
"""
import sys


# list of all posible solutions to the N Queens problem
solutions = []

# size of the chessboard
board_size = 0

# List of posible queen positions on the chessboard
positions = None


def get_input():
    """
    Gets and validates program's argument.

    Returns:
        int: The size of the chessboard.
    """
    global board_size
    board_size = 0
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        board_size = int(sys.argv[1])
    except Exception:
        print("N must be a number")
        sys.exit(1)
    if board_size < 4:
        print("N must be at least 4")
        sys.exit(1)
    return board_size


def is_attacking(q0, q1):
    """
    Checks if the positions of two queens are in an attacking mode.
    Args:
        q0 (list or tuple): The first queen's position.
        q1 (list or tuple): The second queen's position.
    Returns:
        bool: True if the queens are in an attacking position else False.
    """
    if (q0[0] == q1[0]) or (q0[1] == q1[1]):
        return True
    return abs(q0[0] - q1[0]) == abs(q0[1] - q1[1])


def group_exists(group):
    """
    Checks if a group exists in the list of solutions.
    Args:
        group (list of integers): A group of possible positions.
    Returns:
        bool: True if it exists, otherwise False.
    """
    global solutions
    for soln in solutions:
        i = 0
        for soln_pos in soln:
            for group_pos in group:
                if soln_pos[0] == group_pos[1] and soln_pos[1] == group_pos[1]:
                    i += 1
        if i == board_size:
            return True
    return False


def build_solution(row, group):
    """
    Builds a solution for the n queens problem.
    Args:
        row (int): The current row in the chessboard.
        group (list of lists of integers): The group of valid positions.
    """
    global solutions
    global board_size
    if row == board_size:
        tmp0 = group.copy()
        if not group_exists(tmp0):
            solutions.append(tmp0)
    else:
        for col in range(board_size):
            a = (row * board_size) + col
            matches = zip(list([position[a]]) * len(group), group)
            used_positions = map(lambda x: is_attacking(x[0], x[1]), matches)
            group.append(position[a].copy())
            if not any(used_positions):
                build_solution(row + 1, group)
            group.pop(len(group) - 1)


def get_solutions():
    """
    Gets the solutions for the given chessboard size.
    """
    global position, board_size
    position = list(map(
        lambda x: [x // board_size, x % board_size], range(board_size ** 2)))
    a = 0
    group = []
    build_solution(a, group)


board_size = get_input()
get_solutions()
for solution in solutions:
    print(solution)
