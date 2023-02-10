# Problem Link: https://www.codewars.com/kata/5266876b8f4bf2da9b000362


# My Solution:

def likes(names):
    n = len(names)
    if n == 0:
        return "no one likes this"
    elif n == 1:
        return "{} likes this".format(names[0])
    elif n == 2:
        return "{} and {} like this".format(names[0], names[1])
    elif n == 3:
        return "{}, {} and {} like this".format(names[0], names[1], names[2])
    else:
        return "{}, {} and {} others like this".format(names[0], names[1], n - 2)

