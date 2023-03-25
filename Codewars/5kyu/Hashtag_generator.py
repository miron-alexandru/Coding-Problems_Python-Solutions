# Problem Link: https://www.codewars.com/kata/52449b062fb80683ec000024


# Solution:
def generate_hashtag(s):
    words = s.strip().split()
    hashtag = "#" + "".join(word.capitalize() for word in words)
    if not words:
        return False
    
    if len(hashtag) > 140:
        return False
    
    return hashtag