def histogram2(s):
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)

    return d


def invert_dict(d):
    inverse = {}
    for key in d:
        new_key = d[key]
        inverse.setdefault(new_key, []).append(key)
    return inverse


hist = histogram2("parrot")
inverse = invert_dict(hist)
print(inverse)
