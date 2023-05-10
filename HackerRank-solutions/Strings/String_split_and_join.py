# You are given a string. Split the string on a " " (space) delimiter and join
# using a - hyphen.

# Input format
# The one line contains a string consisting of space separated words

# Sample input
# this is a string

# Sample output
# this-is-a-string


# My solution


def split_and_join(line):
    line = line.split(" ")
    line = "-".join(line)
    return line
