# Problem Link: https://www.codewars.com/kata/54bf1c2cd5b56cc47f0007a1


# My Solution:
def duplicate_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
    count = 0
    for char in char_count:
        if char_count[char] > 1:
            count += 1
    return count
