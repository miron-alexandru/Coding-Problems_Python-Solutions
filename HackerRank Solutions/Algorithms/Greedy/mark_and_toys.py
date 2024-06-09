# problem link: https://www.hackerrank.com/challenges/mark-and-toys/problem


# my solution:
def maximumToys(prices, k):
    prices.sort()
    toy_count = 0
    total_cost = 0
    
    for i in prices:
        if i + total_cost < k:
            toy_count += 1
            total_cost += i
            if total_cost  > k:
                break
    return toy_count

# one line solution:
def maximumToys(prices, k):
    return sum(price <= k for price in sorted(prices))
