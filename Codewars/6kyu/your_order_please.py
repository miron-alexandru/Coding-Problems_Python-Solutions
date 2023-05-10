# Problem Link: https://www.codewars.com/kata/55c45be3b2079eccff00010f


# My Solution:
def order(words):
    return " ".join(sorted(words.split(), key=lambda w: sorted(w)))
