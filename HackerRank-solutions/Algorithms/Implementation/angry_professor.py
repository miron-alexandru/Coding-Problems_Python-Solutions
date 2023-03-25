# problem link: https://www.hackerrank.com/challenges/angry-professor/problem


# my solution:
def angryProfessor(k, a):
    count = sum(1 for arrival_time in a if arrival_time <= 0)
    if count < k:
        return "YES"
    else:
        return "NO"