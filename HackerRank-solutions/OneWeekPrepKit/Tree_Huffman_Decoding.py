# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-tree-huffman-decoding/problem


# My Solution:

def decodeHuff(root, s):
    current = root
    ans = []
    for i in range(len(s)):
        if s[i] == '0':
            current = current.left
        else:
            current = current.right
        if current.left is None and current.right is None:
            ans.append(current.data)
            current = root
    print(''.join(ans))
