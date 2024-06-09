# Problem Link: https://www.codewars.com/kata/5264d2b162488dc400000001


# My Solution:


def spin_words(sentence):
    words = sentence.split()
    reversed_word = [word[::-1] if len(word) >= 5 else word for word in words]
    return " ".join(reversed_word)
