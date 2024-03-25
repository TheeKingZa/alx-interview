#!/usr/bin/env python3

import sys
import signal

# Dictionary to store the count of each status code
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}

total_file_size = 0  # Total file size counter
line_count = 0  # Line counter

def print_statistics():
    """Print statistics based on the collected data."""
    global total_file_size
    global status_counts
    print("File size:", total_file_size)
    for code, count in sorted(status_counts.items()):
        if count > 0:
            print(f"{code}: {count}")

def signal_handler(sig, frame):
    """Handle keyboard interruption (CTRL + C)"""
    print_statistics()
    sys.exit(0)

# Register signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Process input line by line
for line in sys.stdin:
    try:
        # Split the line by whitespace
        parts = line.split()

        # Check if the line matches the expected format
        if len(parts) != 10 or parts[3] != '"GET' or parts[5] != 'HTTP/1.1"':
            continue

        # Extract file size and status code
        file_size = int(parts[9])
        status_code = int(parts[8])

        # Update total file size
        total_file_size += file_size

        # Update status code count
        if status_code in status_counts:
            status_counts[status_code] += 1

        # Increment line count
        line_count += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics()

    except Exception as e:
        # Skip line if there's any error
        continue

# Print final statistics
print_statistics()
