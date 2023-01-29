# the user enters a string and a substring. You have to print
# the number of times that the substring occurs in the given string.
# String traversal will take place from left to right, not from right to left.

# Input format
# The first line of input contains the original string.
# The next line contains the substring

# Output Format
# Output the integer number indicating the total number of occurences of
# the substring in the original string 

# Sample Input
# ABCDCDC
# CDC

# Sample Output
# S


# My Solution:

def count_substring(string, substring):
	count = 0
	for i in range(len(string)):
		if string[i:].startswith(substring):
			count += 1
	return count


