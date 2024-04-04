# 0x04. UTF-8 Validation

## Requirements

### General
1. Allowed editors: vi, vim, emacs
2. All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
3. All your files should end with a new line
4. The first line of all your files should be exactly #!/usr/bin/python3
5. A README.md file, at the root of the folder of the project, is mandatory
6. Your code should use the PEP 8 style (version 1.7.x)
7. All your files must be executable

## Tasks
### 0. UTF-8 Validation
Write a method that determines if a given data set represents a valid UTF-8 encoding.

1. Prototype: def validUTF8(data)
2. Return: True if data is a valid UTF-8 encoding, else return False
3. A character in UTF-8 can be 1 to 4 bytes long
4. The data set can contain multiple characters
5. The data will be represented by a list of integers
6. Each integer represents 1 byte of data, therefore you only need to handle the 8 least significant bits of each integer
