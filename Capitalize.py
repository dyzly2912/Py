#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    if not s:
        return s
    chars = list(s)
    for i in range(len(chars)):
        if i == 0 or chars[i-1] == ' ':
            chars[i] = chars[i].upper()
    return ''.join(chars)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
