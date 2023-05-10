# problem link: https://www.hackerrank.com/challenges/bon-appetit/problem


# my solution:
def bonAppetit(bill, k, b):
    total_cost = 0
    for i, cost in enumerate(bill):
        if i != k:
            total_cost += cost
    cost_per_person = total_cost // 2

    if cost_per_person == b:
        print("Bon Appetit")
    else:
        print(b - cost_per_person)
