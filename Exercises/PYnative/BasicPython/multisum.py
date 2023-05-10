def multisum(n1, n2):
    if n1 * n2 <= 1000:
        return n1 * n2
    else:
        return n1 + n2


print(multisum(20, 30))
print(multisum(40, 30))


def multisum2(n1, n2):
    product = n1 * n2
    if product <= 1000:
        return product
    else:
        return n1 + n2


print(multisum2(20, 30))
print(multisum2(40, 30))
