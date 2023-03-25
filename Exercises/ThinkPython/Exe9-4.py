def uses_only(word, letters):
    for letter in word:
        if letter not in letters:
            return False
    return True

fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if uses_only(word, 'a c e f h l o') == True:
        print(word)
        count += 1
        
print(count)
