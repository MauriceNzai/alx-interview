#!/usr/bin/python3

"""
reads stdin line by line and computes metrics:
"""

import re
import signal
import sys


def parse_line(line):
    """
    parses a line of user input
    """
    # input format to match below regular expresssion
    pattern = r'^(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1\.1" (\d+) (\d+)$'

    # match the pattern
    match = re.match(pattern, line)
    if match:
        ip_address = match.group(1)
        date = match.group(2)
        status_code = int(match.group(3))
        file_size = int(match.group(4))

        return ip_address, date, status_code, file_size
    else:
        return None


def print_stats(total_file_size, status_code_count):
    """
    prints the statistics in a given format
    """
    print("File size:", totsl_file_size)
    for status_code in sorted(status_code_count.keys()):
        print("{}: {}".format(status_code, status_code_count[status_code]))


def signal_handler(signal, frame):
    """
    handles signals
    """
    print("\nKeyboard Interruption (CTRL C) detected. Printing statistics.")
    print_statistics(total_file_size, status_code_count)
    sys.exit(0)


def main():
    """
    the entry point and main function
    """
    global total_file_size, status_code_count

    total_file_size = 0
    status_code_count = {}

    # Register signal handler for SIGINT (CTRL C)
    signal.signal(signal.SIGINT, signal_handler)

    try:
        line_count = 0
        for line in sys.stdin:
            line_count += 1
            line = line.strip()
            parsed_data = parse_line(line)

            if parsed_data:
                ip_address, date, status_code, file_size = parsed_data
                total_file_size += file_size
                status_code_count[status_code] = status_code_count.get(
                        status_code, 0) + 1

            # print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_count)

    except KeyboardInterrupt:
        # trigger signal handler for CTRL C
        signal_handler(signal.SIGINT, None)

    except BrokenPipeError:
        # ignore broken pipe error
        pass


if __name__ == "__main__":
    main()
