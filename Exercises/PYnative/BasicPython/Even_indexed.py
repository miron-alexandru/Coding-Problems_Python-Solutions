word = input('Enter a random string: ')
size = len(word)

for i in range(0, size - 1, 2):
	print("index[", i, "]", word[i])


# Using list slicing:

# accept input string from a user
word = input('Enter word ')
print("Original String:", word)

# using list slicing
# convert string to list
# pick only even index chars
x = list(word)
for i in x[0::2]:
    print(i)
