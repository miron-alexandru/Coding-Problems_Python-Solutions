# Problem Link: https://www.codewars.com/kata/5839edaa6754d6fec10000a2


# My solution:
	
def find_missing_letter(letters):
    for i in range(len(letters) - 1):
        if ord(letters[i + 1]) - ord(letters[i]) > 1:
            missing_letter = chr(ord(letters[i]) + 1)
            break
    return missing_letter

