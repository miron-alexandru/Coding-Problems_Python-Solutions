def myfunc(name, age):
    print(name, age)


myfunc("Ake", 23)
print()


def myfunc2(*args):
    for i in args:
        print(i)


myfunc2("Ake", 23, "Hello", "Pitu")

print()


def calculation(a, b):
    add = a + b
    sub = a - b
    return add, sub


res = calculation(40, 10)
print(res)
print()


def calculation(a, b):
    return a + b, a - b


# get result in tuple format
# unpack tuple
add, sub = calculation(40, 10)
print(add, sub)
print()


def show_employee(name, salary=9000):
    print(name, salary)


show_employee("Ake")
show_employee("Ake", 10000)
print()


def outer(a, b):
    def inner(a, b):
        return a + b

    res2 = inner(a, b)
    return res2 + 5


print(outer(5, 10))

print()


def addition(num):
    if num:
        # call same function by reducing number by 1
        return num + addition(num - 1)
    else:
        return 0


res = addition(10)
print(res)

print()


def display_student(name, age):
    print(name, age)


show_student = display_student

show_student("Emma", 26)
print()

print(list(range(4, 30, 2)))
print()
x = [4, 6, 8, 24, 12, 2]
print(max(x))
