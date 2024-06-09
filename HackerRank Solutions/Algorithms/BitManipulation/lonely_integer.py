# problem link: https://www.hackerrank.com/challenges/lonely-integer/problem


# my solution:

def lonelyinteger(a):
    unique_element = 0
    for num in a:
        unique_element ^= num
    return unique_element