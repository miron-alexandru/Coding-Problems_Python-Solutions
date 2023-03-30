# problem link: https://www.hackerrank.com/challenges/validating-named-email-addresses/problem


# my solution:
import re
import email.utils 

n = int(input())


for i in range(0, n):
    pattern = r'^[a-z][\w\-\.]+@[a-z]+\.[a-z]{1,3}$'
    parsed_addr = email.utils.parseaddr(input())
    if re.search(pattern, parsed_addr[1]):
        print(email.utils.formataddr(parsed_addr))