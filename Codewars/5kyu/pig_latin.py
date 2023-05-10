# Problem Link: https://www.codewars.com/kata/520b9d2ad5c005041100000f


# My Solution:
def pig_it(text):
    result = []
    for word in text.split():
        if word.isalpha():
            pig = word[1:] + word[0] + "ay"
            result.append(pig)
        else:
            result.append(word)
    return " ".join(result)
