# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem


# my solution:
import heapq

def cookies(k, A):
    heapq.heapify(A)
    operatios = 0

    while len(A) > 1 and A[0] < k:
        # combine two cookies
        combined_cookie = heapq.heappop(A) + 2 * heapq.heappop(A)

        heapq.heappush(A, combined_cookie)
        
        # Increment the number of operations
        operatios += 1

    if A[0] >= k:
        return operatios
    else:
        return -1
