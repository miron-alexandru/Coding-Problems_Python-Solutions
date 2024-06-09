def print_n(s, n):
    while n > 0:
        print(s)
        n = n - 1


print_n("Ake", 5)


def print_n2(s, n):
    if n <= 0:
        return
    print(s)
    print_n2(s, n - 1)


print_n2("Bebe", 5)
