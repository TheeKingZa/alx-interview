# Log Parsing Script

This script reads log data from standard input (stdin), parses each line according to a specified format, and computes various metrics based on the log data.
---

[`^`](#log-parsing-script)

---
# Functionality
The script performs the following tasks:

1. Reads log data line by line from stdin.
2. Parses each line to extract information such as IP address, date, HTTP method, status code, and file size.
3. Computes the following metrics:
    * Total file size: Sum of the file sizes from all parsed log lines.
    * Number of lines by status code: Counts the occurrences of different HTTP status codes (200, 301, 400, 401, 403, 404, 405, 500) in the parsed log lines.
4. Prints the computed metrics after every 10 lines of log data or upon receiving a keyboard interruption (CTRL + C).
---

[`^`](#log-parsing-script)

---
# Usage
To use the script, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Save the script in a file named log_parser.py.
3. Make the script executable by running chmod +x log_parser.py.
4. Generate log data using the provided generator script (0-generator.py), piping the output to the log parser script:

Bash
```
    ./0-generator.py | ./log_parser.py
```
---

[`^`](#log-parsing-script)

---
5. View the computed metrics printed to the console.


Example: 
Here's an example of the script's output:

```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
# Output truncated for brevity...

```

---

[`^`](#log-parsing-script)

---

# How It Works
The script works by reading log data line by line from stdin. It then splits each line into individual fields and extracts the relevant information, such as the file size and status code. The script maintains counters for the total file size and the occurrences of each status code. After processing every 10 lines or upon receiving a keyboard interruption, the script prints the computed metrics to the console.
---

[`^`](#log-parsing-script)

---
# Notes
The script assumes that the input log data follows a specific format, as described in the problem statement. Lines that do not match this format are skipped.
The script handles keyboard interruptions gracefully by printing the computed metrics before exiting.

---

[`^`](#log-parsing-script)

---