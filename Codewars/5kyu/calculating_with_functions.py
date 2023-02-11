# Problem Link: 


# My Solution:
def zero(func=None):
    return 0 if func is None else func(0)

def one(func=None):
    return 1 if func is None else func(1)

def two(func=None):
    return 2 if func is None else func(2)

def three(func=None):
    return 3 if func is None else func(3)

def four(func=None):
    return 4 if func is None else func(4)

def five(func=None):
    return 5 if func is None else func(5)

def six(func=None):
    return 6 if func is None else func(6)

def seven(func=None):
    return 7 if func is None else func(7)

def eight(func=None):
    return 8 if func is None else func(8)

def nine(func=None):
    return 9 if func is None else func(9)

def plus(y):
    def inner(x):
        return x + y
    return inner

def minus(y):
    def inner(x):
        return x - y
    return inner

def times(y):
    def inner(x):
        return x * y
    return inner

def divided_by(y):
    def inner(x):
        return x // y
    return inner