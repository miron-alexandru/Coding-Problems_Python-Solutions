# Problem Link: https://www.codewars.com/kata/514b92a657cdc65150000006


# My Solution: 
def solution(number):
    sol = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sol += i
        elif number < 0:
            return 0
        
    return sol
