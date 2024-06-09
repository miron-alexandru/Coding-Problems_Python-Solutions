# problem link: https://www.hackerrank.com/challenges/tutorial-intro/problem


# my solution:
def introTutorial(V, arr):
    for i, value in enumerate(arr):
        if value == V:
            return i
