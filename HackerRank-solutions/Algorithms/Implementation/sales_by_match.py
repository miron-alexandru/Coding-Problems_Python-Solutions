# problem link: https://www.hackerrank.com/challenges/drawing-book/problem


# my solution:
def sockMerchant(n, ar):
    sock_dict = {}
    # for each sock check if the color is already in the dict.
    for s in ar:
        if s in sock_dict:
            sock_dict[s] += 1
        else:
            sock_dict[s] = 1
    # calculate how many pairs of socks there are for each color.
    pairs = 0
    for c in sock_dict.values():
        pairs += c // 2
    
    return pairs