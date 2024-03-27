# 0x03. Log Parsing

## Concepts Needed:
1. File I/O in Python: Understand how to read from sys.stdin line by line.
2. Signal Handling in Python: Handling keyboard interruption (CTRL + C) using signal handling in Python.
3. Data Processing: 
	a. Parsing strings to extract specific data points.
	b. Aggregating data to compute summaries.
4. Regular Expressions: Using regular expressions to validate the format of each line.
5. Dictionaries in Python: Using dictionaries to count occurrences of status codes and accumulate file sizes.
6. Exception Handling: Handling possible exceptions that may arise during file reading and data processing.

## Requirements
### General
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the PEP 8 style (version 1.7.x)
7. All your files must be executable
8. The length of your files will be tested using wc

## Tasks
### 0. Log parsing

Write a script that reads stdin line by line and computes metrics:

1. Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size> (if the format is not this one, the line must be skipped)
2. After every 10 lines and/or a keyboard interruption (CTRL + C), print these statistics from the beginning:
	a. Total file size: File size: <total size>
	b. where <total size> is the sum of all previous <file size> (see input format above)
	c. Number of lines by status code:
		i.possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
		ii. if a status code doesn’t appear or is not an integer, don’t print anything for this status code
		iii. format: <status code>: <number>
		iv. status codes should be printed in ascending order


Warning: In this sample, you will have random value - it’s normal to not have the same output as this one.
