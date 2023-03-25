def back(s):
	index = len(s) - 1
	while index > 0:
		letter = s[index]
		print(letter)
		index = index - 1

back('banana')

print()


def back2(s):
	print('\n'.join(reversed(s)))

back2('banana')
print()

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
		if letter in ('O', 'Q'):  # if the letter is O or Q
			print(letter + 'u' + suffix)
		else:
			print(letter + suffix)

print()


def find(word, letter, ind):
	index = ind
	while index < len(word):
		if word[index] == letter:
			return index
		index = index + 1
	return - 1

print(find('banana', 'a', 2 ))
print()

def count(s, l):
	count = 0
	for letter in s:
		if letter == l:
			count = count + 1
	print(count)

count('banana', 'n')
print()

# Usign three parameters
def find_count(srch_wrd, srch_char, startlookingat):
	counter = 0
	index = startlookingat

	while index < len(srch_wrd):     
		if srch_wrd[index] == srch_char:
			counter += 1
		index += 1 
	return counter

print(find_count('banana', 'a', 4))
print()

#Using Find
def counter2(word, letter):
	result = 0
	startat = 0
	while startat < len(word):
		next_letter_position = find(word, letter, startat)
		if next_letter_position != -1:
			result += 1
			startat = next_letter_position + 1
		else:
			break
	return result

print(counter2('banana', 'a'))
