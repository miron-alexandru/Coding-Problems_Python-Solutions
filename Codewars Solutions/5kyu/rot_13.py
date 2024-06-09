# Problem Link: https://www.codewars.com/kata/530e15517bc88ac656000716


# My Solution:
def rot13(message):
    look = str.maketrans(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz",
        "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm",
    )

    return message.translate(look)
