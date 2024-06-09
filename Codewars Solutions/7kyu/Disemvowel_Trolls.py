# Problem Link: https://www.codewars.com/kata/52fba66badcd10859f00097e


# My Solution:
def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i, "")
    return string_
