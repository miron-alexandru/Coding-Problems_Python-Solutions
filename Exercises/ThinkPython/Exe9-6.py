def is_abecedarian(word):
    previous_letter = word[0]
    for letter in word:
        if ord(letter) < ord(previous_letter):
            return False
        previous_letter = letter
    return True


fin = open('words.txt')
count = 0

for line in fin:
    word = line.strip()
    if is_abecedarian(word) == True:
        print(word)
        count += 1
print(count)
