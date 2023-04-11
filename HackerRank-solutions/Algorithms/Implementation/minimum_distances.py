# problem link: https://www.hackerrank.com/challenges/minimum-distances/problem


# my solution:
def minimumDistances(a):
    distances = {}
    min_distance = len(a)
    
    for i in range(len(a)):
        if a[i] in distances:
            distance = i - distances[a[i]]
            min_distance = min(min_distance, distance)
        distances[a[i]] = i
    
    if min_distance == len(a):
        return -1
    else:
        return min_distance
