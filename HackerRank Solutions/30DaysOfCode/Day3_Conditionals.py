# Problem link: https://www.hackerrank.com/challenges/30-conditional-statements/problem


# My Solution:
if __name__ == "__main__":
    n = int(input().strip())
    if n % 2 != 0:
        print("Weird")
    elif n in range(2, 6) and n % 2 == 0:
        print("Not Weird")
    elif n in range(6, 21) and n % 2 == 0:
        print("Weird")
    elif n > 20 and n % 2 == 0:
        print("Not Weird")
