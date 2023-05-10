def has_no_e(word):
    for letter in word:
        if letter == "e":
            return False
    return True


print(has_no_e("bebe"))

count = 0
num_of_words = 113809
file = open("words.txt")

for line in file:
    word = line.strip()
    if has_no_e(word) == True:
        count += 1
        print(word)
print()

print(count / num_of_words * 100, "%")
