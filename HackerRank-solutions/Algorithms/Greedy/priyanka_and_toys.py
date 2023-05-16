# problem link: https://www.hackerrank.com/challenges/priyanka-and-toys/problem


# my solution:
def toys(w):
    w.sort()
    min_weight = w[0]
    container_count = 1
    
    for i in w[1:]:
        if i > min_weight + 4:
            min_weight = i
            container_count += 1
    return container_count
        