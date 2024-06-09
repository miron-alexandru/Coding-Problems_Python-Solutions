def print_n(s, n):
    if n <= 0:
        return
    print(s)
    print_n(s, n - 1)


# print_n('Hello', 2)


def do_n(f, s, n):
    for i in range(n):
        f(s, n)


do_n(print_n, "Hello", 2)
