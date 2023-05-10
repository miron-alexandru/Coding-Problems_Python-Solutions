# You are given a string S with width w.
# Your task is to wrap the string into a paragraph of width w.

# wrap has the following parameters:

# string string: a long string
# int max_width: the width to wrap to

# Returns
# string: a single string with newline characters ('\n') where the breaks
# should be


# Input format
# Teh first line contains a string, string
# The second line contains the width, maxwidth

# Sample Input
# ABCDEFGHIJKLIMNOQRSTUVWXYZ
# 4


# Sample Output
# ABCD
# EFGH
# IJKL
# IMNO
# QRST
# UVWX
# YZ


# My Solution

import textwrap


def wrap(string, max_width):
    return textwrap.fill(string, max_width)
