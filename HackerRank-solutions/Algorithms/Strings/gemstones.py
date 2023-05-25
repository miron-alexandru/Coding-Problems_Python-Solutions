# problem link: https://www.hackerrank.com/challenges/gem-stones/problem


# My solution:

def gemstones(arr):
	gemstones_num = set(arr[0])

    for rock in arr[1:]:
        gemstones_num.intersection_update(rock)
    
    return len(gemstones_num)