def avoids(word, letters):
    for letter in word:
        if letter in letters:
            return False
    return True


print(avoids("bebe", "be"))

file = open("words.txt")
count = 0

forbidden_l = input("Type forbidden letters: ")

for line in file:
    word = line.strip()
    if avoids(word, forbidden_l) == True:
        count += 1

print(count)
