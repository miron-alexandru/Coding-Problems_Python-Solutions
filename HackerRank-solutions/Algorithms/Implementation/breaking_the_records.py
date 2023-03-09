# Problem Link: https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem

# My Solution:

def breakingRecords(scores):
    min_score = max_score = scores[0]
    min_count = max_count = 0
    
    for score in scores[1:]:
        if score < min_score:
            min_score = score
            min_count += 1
        elif score > max_score:
            max_score = score
            max_count += 1
    
    return [max_count, min_count]
