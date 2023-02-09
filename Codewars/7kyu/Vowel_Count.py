# Problem Link: https://www.codewars.com/kata/54ff3102c1bad923760001f3


# My solution: 
def get_count(sentence):
    count = 0
    for char in sentence:
        if char in 'aeiouAEIOU':
            count += 1
        else:
            continue
    return count
