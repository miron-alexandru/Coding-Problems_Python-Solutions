def is_triangle(a, b, c):
    if (a + b >= c) and (a + c >= b) and (b + c >= a):
        print("Yes")
    else:
        print("No")


def prompting():
    side1 = int(input("Enter length 1: "))
    side2 = int(input("Enter length 2: "))
    side3 = int(input("Enter length 3: "))

    is_triangle(side1, side2, side3)


prompting()
