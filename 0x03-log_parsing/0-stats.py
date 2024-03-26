#!/usr/bin/python3

import sys
import signal
import re

# Define variables to store statistics
total_file_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_statistics():
    """
    Print current statistics including total file size and counts for each status code.
    """
    # Print total file size and counts for each status code
    global total_file_size, status_counts
    print("File size: {}".format(total_file_size))
    for status_code, count in sorted(status_counts.items()):
        if count > 0:
            print("{}: {}".format(status_code, count))

def parse_line(line):
    """
    Extract status code and file size from the line using regular expressions.
    Update total file size and status counts accordingly.
    """
    # Extract status code and file size from the line using regex
    global total_file_size, status_counts
    match = re.match(r'^\d+\.\d+\.\d+\.\d+ - \[.*\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)$', line)
    if match:
        status_code = int(match.group(1))
        file_size = int(match.group(2))
        # Update total file size
        total_file_size += file_size
        # Update status count
        if status_code in status_counts:
            status_counts[status_code] += 1

def signal_handler(sig, frame):
    """
    Signal handler function to print statistics on keyboard interruption.
    """
    # Print statistics on keyboard interruption
    print_statistics()
    sys.exit(0)

# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read from stdin line by line
for line in sys.stdin:
    # Parse each line and update statistics
    parse_line(line.strip())
    line_count += 1
    # Print statistics every 10 lines
    if line_count % 10 == 0:
        print_statistics()
