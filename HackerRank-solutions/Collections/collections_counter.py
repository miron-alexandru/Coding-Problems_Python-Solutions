"""
Raghu is a shoe shop owner. His shop has x number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay xi amount of 
money only if they get the shoe of their desired size.
Your task is to compute how much money Raghu earned.


Input format
The first line contains X. the number of shes.
The second line contains the space separated list of all the shoe sizez
in the shop
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size
deired by the customer and xi, the price of the shoe.


Output format
Print the amount of money earned by Raghu


Sample input
10
2 3 4 5 6 8 7 6 5 18
6
6 55
6 45
6 55
4 40
18 60
10 50

Sample Output
200
"""
# My solution:

from collections import Counter

x = int(input())
shoes = Counter(map(int, input().split()))
money = 0

for i in range(int(input())):
    size, price = map(int, input().split())
    if shoes[size]:
        money += price
        shoes[size] -= 1

print(money)
