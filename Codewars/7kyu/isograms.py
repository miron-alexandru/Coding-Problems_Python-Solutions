# Problem Link: https://www.codewars.com/kata/54ba84be607a92aa900000f1


# My Solution:
def is_isogram(string):
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
