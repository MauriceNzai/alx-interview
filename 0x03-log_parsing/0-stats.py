#!/usr/bin/python3

"""
reads stdin line by line and computes metrics:
"""

import sys


i = 0
sum_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0,
                '405': 0, '500': 0}

try:
    for line in sys.stdin:
        args = line.split(" ")
        if len(args) > 2:
            status_value = args[-2]
            file_size = args[-1]
            if status_value in status_codes:
                status_codes[status_value] += 1
            total_file_size += int(file_sizie)
            i = i + 1
            if i == 10:
                print("File size: {:d}".format(total_file_size))
                sorted_keys = sorted(status_codes.keys())
                for key in sorted_keys:
                    val = status_codes[key]
                    if val != 0:
                        print("{}: {}".format(key, val))
                i = 0
except Exception:
    pass
