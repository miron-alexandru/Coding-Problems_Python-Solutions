# Problem Link: https://www.hackerrank.com/challenges/30-more-exceptions/problem


# My Solution:
class Calculator:
    def __init__(self, n=0, p=0):
        self.n = n
        self.p = p
        
    def power(self, n, p):
        if n < 0 or p < 0:
            raise ValueError('n and p should be non-negative')
        return n ** p
