# Problem Link:  https://www.codewars.com/kata/526989a41034285187000de4


# My Solution:
import ipaddress


def ips_between(start, end):
    start_ip = int(ipaddress.IPv4Address(start))
    end_ip = int(ipaddress.IPv4Address(end))
    return end_ip - start_ip
