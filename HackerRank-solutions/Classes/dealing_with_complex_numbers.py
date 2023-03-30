# problem link: https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem


# my solution:

import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)
    
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imaginary - other.imaginary)
        
    def __mul__(self, other):
        return Complex(self.real * other.real - self.imaginary * other.imaginary, 
                       self.real*other.imaginary + self.imaginary*other.real)
    
    def __truediv__(self, other):
        denominator = other.real ** 2 + other.imaginary ** 2
        return Complex((self.real * other.real + self.imaginary * other.imaginary) / denominator, 
                       (self.imaginary*other.real - self.real * other.imaginary) / denominator)
        
    def mod(self):
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result