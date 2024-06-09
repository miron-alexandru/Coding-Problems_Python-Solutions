# problem link: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem


# my solution:
def catAndMouse(x, y, z):
    dist_cat_a = abs(z - x)
    dist_cat_b = abs(z - y)

    if dist_cat_a < dist_cat_b:
        return "Cat A"
    elif dist_cat_b < dist_cat_a:
        return "Cat B"
    else:
        return "Mouse C"
