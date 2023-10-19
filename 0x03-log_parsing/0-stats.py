#!/usr/bin/python3

import sys


def print_metrics(status_codes, total_file_size):
    """
    Method to print the metrics
    """

    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


total_file_size = 0
code = 0
counter = 0
status_codes = {"200": 0,
                "301": 0,
                "400": 0,
                "401": 0,
                "403": 0,
                "404": 0,
                "405": 0,
                "500": 0}

try:
    for line in sys.stdin:
        trimmed_line = line.split()
        inverted_line = trimmed_line[::-1]

        if len(inverted_line) > 2:
            counter += 1

            if (counter <= 10):
                total_file_size += int(inverted_line[0])
                code = inverted_line[1]

                if (code in status_codes.keys()):
                    status_codes[code] += 1

            if (counter == 10):
                print_metrics(status_codes, total_file_size)
                counter = 0

finally:
    print_metrics(status_codes, total_file_size)
