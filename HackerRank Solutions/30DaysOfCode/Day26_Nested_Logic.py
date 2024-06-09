# Problem Link: https://www.hackerrank.com/challenges/30-nested-logic/problem

# My Solution:
returned_date = list(map(int, input().split()))
due_date = list(map(int, input().split()))

if returned_date[2] < due_date[2]:
    fine = 0
elif returned_date[2] > due_date[2]:
    fine = 10000
elif returned_date[1] > due_date[1]:
    fine = (returned_date[1] - due_date[1]) * 500
elif returned_date[0] > due_date[0]:
    fine = (returned_date[0] - due_date[0]) * 15
else:
    fine = 0

print(fine)
