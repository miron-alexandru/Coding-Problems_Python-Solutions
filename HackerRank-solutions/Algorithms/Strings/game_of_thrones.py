# problem link: https://www.hackerrank.com/challenges/game-of-thrones/problem


# my solution:
def gameOfThrones(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    odd_count = 0
    for count in char_counts.values():
        if count % 2 != 0:
            odd_count += 1
        if odd_count > 1:
            return "NO"
    
    return "YES"





s = 'aabbccdd'
print(gameOfThrones(s))

