#!/usr/bin/python3

import sys
import signal
import re

# regex pattern to match input format
pattern = '^(\S+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$'
re_compiled = re.compile(pattern)

# metrics to track
file_size_total = 0
status_codes = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_count = 0

def print_metrics():
    # print total file size
    print("Total file size: {}".format(file_size_total))
    # print status codes
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def signal_handler(sig, frame):
    # print metrics when interrupted
    print_metrics()
    sys.exit(0)


# bind Ctrl+C interruption signal to the handler
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        match = re_compiled.match(line)
        if match is not None:
            file_size = int(match.group(4)) # get file size from regex group
            status_code = match.group(3) # get status code from regex group
            file_size_total += file_size
            if status_code in status_codes:
                status_codes[status_code] += 1
            line_count += 1
            if line_count % 10 == 0:
                print_metrics()
except KeyboardInterrupt:
    pass
