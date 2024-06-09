def store_dict(file):
    d = dict()
    file = open(file)
    words = (word for line in file.readlines() for word in line.split())
    d = {i: word for i, word in enumerate(words)}
    print(d)


print(store_dict("words.txt"))
