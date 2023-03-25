# Problem link: https://www.hackerrank.com/challenges/py-collections-ordereddict/problem


# My solution:

from collections import OrderedDict

n = int(input().strip())
od = OrderedDict()

for i in range(n):
    values = input().strip().split()
    item = ' '.join(values[:-1])
    price = int(values[-1])
    if item in od:
        od[item] += price
    else:
        od[item] = price

for item, price in od.items():
    print(item, price)
