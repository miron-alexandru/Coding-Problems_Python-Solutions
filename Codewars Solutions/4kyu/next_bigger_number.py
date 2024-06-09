# Problem Link: https://www.codewars.com/kata/55983863da40caa2c900004e


# My Solution:
def next_bigger(n):
    digits = list(str(n))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = len(digits) - 1
    while digits[j] <= digits[i]:
        j -= 1

    # Swap digits
    digits[i], digits[j] = digits[j], digits[i]
    # Reverse
    digits[i + 1 :] = reversed(digits[i + 1 :])

    return int("".join(digits))
