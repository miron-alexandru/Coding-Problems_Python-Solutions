# problem link: https://www.hackerrank.com/challenges/ginorts/problem

# my solution:
# Read the input
s = input()

# Define a function to determine the sorting order of a character
def get_sort_order(c):
    if c.islower():
        return ord(c) - ord('a')
    elif c.isupper():
        return ord(c) - ord('A') + 26
    elif c.isdigit():
        if int(c) % 2 == 1:
            return ord(c) - ord('0') + 52
        else:
            return ord(c) - ord('0') + 62

# Sort the characters in the string based on the sorting order
sorted_s = sorted(s, key=get_sort_order)

print(''.join(sorted_s))
