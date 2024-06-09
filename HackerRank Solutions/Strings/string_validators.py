# You are given a string s.
# Your task is to find out if the string s contains:
# alphanumeric characters, alphabetical characters, digits,
# lowercase and uppercase characters.

# Input Format
# A single line containing a string S

# Output format
# In the first line, print True if s has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if s has any alphabetical characters. Otherwise, print False.
# In the third line, print True if s has any digits. Otherwise, print False.
# In the fourth line, print True if s has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if s has any uppercase characters. Otherwise, print False.

# Sample Input
# qA2

# Sample Output
# True
# True
# True
# True
# True


if __name__ == "__main__":
    s = input()
    print(any(char.isalnum() for char in s))
    print(any(char.isalpha() for char in s))
    print(any(char.isdigit() for char in s))
    print(any(char.islower() for char in s))
    print(any(char.isupper() for char in s))
