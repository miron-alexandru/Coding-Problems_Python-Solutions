# problem link: https://www.hackerrank.com/challenges/strange-advertising/problem

# my solution:
def viralAdvertising(n):
    shared = 5
    liked = 2
    cumulative = 2
    for i in range(2, n + 1):
        shared = liked * 3
        liked = shared // 2
        cumulative += liked
    return cumulative