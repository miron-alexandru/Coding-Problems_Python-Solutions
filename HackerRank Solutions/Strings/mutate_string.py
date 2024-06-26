# Read a given string, change the character at a given index
# and then print the modified string

# Function Description
# mutate_string has the following parameters:

# string string: the string to change
# int position: the index to insert the character at
# string character: the character to insert

# Returns

# string: the altered string

# Input Format
# The first line contains a string, string
# The next line contains an integer position,
# the index location and a string character separated by a space

# Sample Input
# abracadabra 5 k

# Sample Output
# abrackdabra


# My Solutions:

# Solution:


def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    string = "".join(l)
    return string
