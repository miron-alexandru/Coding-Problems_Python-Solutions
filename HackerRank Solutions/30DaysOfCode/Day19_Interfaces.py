# Problem Link: https://www.hackerrank.com/challenges/30-interfaces/problem


# My Solution:


class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        divisors = []
        for i in range(1, n // 2 + 1):
            if n % i == 0:
                divisors.append(i)
        divisors.append(n)
        return sum(divisors)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)
