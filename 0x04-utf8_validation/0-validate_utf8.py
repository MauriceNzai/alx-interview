#!/usr/bin/python3
"""
Module for determining valid UTF-8 encoding
REF: See <https://datatracker.ietf.org/doc/html/rfc3629#page-4>
"""


def validUTF8(data):
    """
    determines if input data is valid UTF-8 encoding or not
    Args:
        data :- the input to be checked (a list of integers)
    """
    nbytes = 0

    b1 = 1 << 7
    b2 = 1 << 6

    for i in data:
        b = 1 << 7
        if nbytes == 0:
            while b & i:
                nbytes += 1
                b = b >> 1
            if nbytes == 0:
                continue
            if nbytes == 1 or nbytes > 4:
                return False
        else:
            if not (i & b1 and not (i & b2)):
                return False
        nbytes -= 1
    return nbytes == 0
