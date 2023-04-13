# problem link: https://www.hackerrank.com/challenges/apple-and-orange/problem


# my solution:
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apples_count = 0
    oranges_count = 0
    for d in apples:
        dist = a + d
        if s <= dist <= t:
            apples_count += 1
    for d in oranges:
        dist = b + d
        if s <= dist <= t:
            oranges_count += 1
    print(apples_count, oranges_count, sep='\n')