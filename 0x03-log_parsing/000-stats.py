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
    print("File size:", total_file_size)
    for status_code in sorted(status_code_count.keys()):
        print("{}: {}".format(status_code, status_code_count[status_code]))


def signal_handler(signal, frame):
    """
    handles signals
    """
    print_stats(total_file_size, status_code_count)
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
        for line_count, line in enumerate(sys.stdin, 1):
            line = line.strip()
            parsed_data = parse_line(line)

            if parsed_data:
                ip_address, date, status_code, file_size = parsed_data
                total_file_size += file_size
                status_code_count[status_code] = status_code_count.get(
                        status_code, 0) + 1

            if line_count % 10 == 0:
                print_stats(total_file_size, status_code_count)

    except KeyboardInterrupt:
        # handle keyboard interruption within the block
        print_stats(total_file_size, status_code_count)
        sys.exit(0)

    except BrokenPipeError:
        # ignore broken pipe error
        pass

    # Print statistics at the end of input
    print("\nEnd of input. Printing final statistics:")
    print_stats(total_file_size, status_code_count)


if __name__ == "__main__":
    main()
