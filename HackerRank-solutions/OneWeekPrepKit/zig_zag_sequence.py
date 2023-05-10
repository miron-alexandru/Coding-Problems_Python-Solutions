# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-zig-zag-sequence/problem


# My Solution:
def findZigZagSequence(a, n):
    a.sort()
    mid = int((n - 1) / 2)
    a[mid], a[n - 1] = a[n - 1], a[mid]

    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return
