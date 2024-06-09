# Problem link: https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem


# my solution:
def minimumBribes(q):
    count = 0
    for i in range(len(q) - 1, -1, -1):
        # Check if this pers bribed more than two people
        if q[i] - (i + 1) > 2:
            print("Too chaotic")
            return
        # count num of people who bribed this pers
        for j in range(max(0, q[i] - 2), i):
            if q[j] > q[i]:
                count += 1

    print(count)
