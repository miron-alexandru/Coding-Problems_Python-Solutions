# Problem Link: https://www.codewars.com/kata/52e88b39ffb6ac53a400022e

# My Solution:
import socket, struct


def int32_to_ip(int32):
    return socket.inet_ntoa(struct.pack('!L', int32))
