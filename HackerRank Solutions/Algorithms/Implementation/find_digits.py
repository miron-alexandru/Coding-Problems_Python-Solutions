# problem link: https://www.hackerrank.com/challenges/find-digits/problem


# my solution:
def findDigits(n):
    # convert int to str
    n_str = str(n)
    count = 0

    for digit_str in n_str:
        digit = int(digit_str)

        # check if digit is not 0 and is a divisor of n
        if digit != 0 and n % digit == 0:
            count += 1

    return count
