# problem link: https://www.hackerrank.com/challenges/append-and-delete/problem


# my solution:
def appendAndDelete(s, t, k):
    pref_len = 0

    for i in range(min(len(s), len(t))):
        if s[i] != t[i]:
            break
        pref_len += 1

    delete_moves = len(s) - pref_len
    add_moves = len(t) - pref_len
    total = delete_moves + add_moves

    if total > k:
        return "No"
    if total % 2 == k % 2:
        return "Yes"
    if len(s) + len(t) <= k:
        return "Yes"

    return "No"
