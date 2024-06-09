# Problem link: https://www.codewars.com/kata/554b4ac871d6813a03000035


# My Solution:
def high_and_low(numbers):
    numbers = [int(num) for num in numbers.split(" ")]
    return str(max(numbers)) + " " + str(min(numbers))
