"""
You are given an integer, N. Your task is to print an alphabet rangoli
of size N.

Te center of the rangoli has the first alphabet letter a, and
the boundary has the Nth alphabet letter (in alphabetical order).

Complete the rangoli function:
parameters:
int size: the size of the rangoli

Returns
String: a single string made up of each of the lines of the
rangoli separated by a newline  character.


Input format
Only one line of input containing the size of the rangoli.


Sample input
5

Sample Output
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""


# My solution:
def print_rangoli(size):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    data = [alpha[i] for i in range(size)]
    items = list(range(size))
    items = items[:-1] + items[::-1]
    for i in items:
        temp = data[-(i + 1) :]
        row = temp[::-1] + temp[1:]
        print("-".join(row).center(n * 4 - 3, "-"))
