import string
alphabet = set(string.ascii_lowercase)

def is_pangram(sentence):
	return set(sentence.lower()) >= alphabet

def is_isogram(string):
	for elem in string:
		if elem.isalpha() and string.count(elem) > 1:
			print("True")

print(is_isogram('lumberjacks'))