# Problem Link: https://www.hackerrank.com/challenges/30-scope/problem


# My Solution:
class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    def computeDifference(self):
        self.maximumDifference = abs(max(self.__elements) - min(self.__elements))


# End of Difference class

_ = input()
a = [int(e) for e in input().split(" ")]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
