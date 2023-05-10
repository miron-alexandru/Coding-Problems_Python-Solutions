# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem


# my solution:
# without recursion
def superDigit(n, k):
    # calculate sum of the digits of n
    x = sum(int(d) for d in n) * k

    # calculate the super digit of x
    while x > 9:
        x = sum(int(d) for d in str(x))

    return x


# with recursion
def superDigit(n, k):
    # If n has only one digit and k is 1, return the digit
    if len(n) == 1 and k == 1:
        return int(n)

    # else, calculate the sum of the digits of n
    s = sum(int(d) for d in n)

    # return the super digit
    return superDigit(str(s * k), 1)
