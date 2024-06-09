# problem link: https://www.hackerrank.com/challenges/taum-and-bday/problem


# my solution:
def taumBday(b, w, bc, wc, z):
    if bc > wc + z:
        cost = (w * wc) + (b * (wc + z))
    elif wc > bc + z:
        cost = (b * bc) + (w * (bc + z))
    else:
        cost = (b * bc) + (w * wc)
    return cost