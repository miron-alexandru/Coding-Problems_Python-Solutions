def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


h = histogram("brontosaurus")
print(h)


def histogram2(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)

    return d


print()


h = histogram2("brontosaurus")
print(h)
