# Problem link: https://www.hackerrank.com/challenges/30-binary-numbers/problem


# My solution:
def consecutiveOnes(n):
    binary = bin(n)[2:] # convert to binary and remove the '0b' prefix
    max_count = 0
    count = 0
    for digit in binary:
        if digit == '1':
            count += 1
        else:
            max_count = max(max_count, count)
            count = 0
    return max(max_count, count)


if __name__ == '__main__':
    n = int(input().strip())
    print(consecutiveOnes(n))