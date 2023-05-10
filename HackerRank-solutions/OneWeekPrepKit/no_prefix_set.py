# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-no-prefix-set/problem


# solution (not mine)


def noPrefix(words):
    dict = {}
    for i in range(len(words)):
        start = dict
        for j in range(len(words[i])):
            if words[i][j] not in start:
                start[words[i][j]] = {}
            start = start[words[i][j]]
            if "*" in list(start.keys()) or (j == len(words[i]) - 1 and (start)):
                print("BAD SET\n", words[i], sep="")
                return
        start["*"] = True
    print("GOOD SET")
