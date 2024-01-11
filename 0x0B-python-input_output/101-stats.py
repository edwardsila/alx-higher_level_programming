#!/usr/bin/python3

"""
reads stdin line by line and computes metrics:
"""
import sys


def print_stats(status_codes, file_size):
    """ reads stdin line by line and computes metrics: """
    print("File size: {}".format(file_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


status_codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}
file_size = 0
line_count = 0

try:
    for line in sys.stdin:
        data = line.split()
        status_code = data[-2]
        file_size += int(data[-1])
        if status_code in status_codes:
            status_codes[status_code] += 1
        line_count += 1
        if line_count % 10 == 0:
            print_stats(status_codes, file_size)
except KeyboardInterrupt:
    print_stats(status_codes, file_size)
    raise
print_stats(status_codes, file_size)
