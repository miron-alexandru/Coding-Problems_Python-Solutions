# problem link: https://www.hackerrank.com/challenges/counting-valleys/problem

# my solution:
def countingValleys(steps, path):
    lv = 0
    count = 0
    for step in path:
        if step == 'U':
            lv += 1
            if lv == 0:
                count += 1
        else:
            lv -= 1
    return count