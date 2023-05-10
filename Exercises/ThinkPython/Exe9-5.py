def uses_all(word, letters):
    required = letters.split()
    for letter in required:
        if letter not in word:
            return False
    return True


file = open("words.txt")
count = 0

for line in file:
    word = line.strip()
    if uses_all(word, "a e i o u y") == True:
        print(word)
        count += 1
print(count)
