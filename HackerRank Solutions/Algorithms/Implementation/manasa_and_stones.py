# problem link: https://www.hackerrank.com/challenges/manasa-and-stones/problem


# my solution:
def stones(n, a, b):
    results = []
    
    last_stone = (n - 1) * min(a, b)
    diff = abs(a - b)
        
    results.extend(sorted(set([last_stone + j * diff for j in range(n)])))
    
    return results
