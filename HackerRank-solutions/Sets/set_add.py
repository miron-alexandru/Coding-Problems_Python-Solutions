'''
Rupal has a huge collection of country stamps.She decided to count the
total number of distinct country stamps in her collection. She asked for
your help. You pick the stamps one by one from a stack of n country stamps.

Find the total number of distinct country stamps

Input format
The first line  contains an integer N, the total number of country stamps.
The next N lines contains the name of the country where the stamp is from.


Output format
The total number of distinct country stamps on a single line.


Sample input
7
UK
China
USA
France
New Zealand
UK
France 

Sample output
5
'''

# My solution

def count_distinct_stamps(n, stamps):
    stamps_set = set()
    for i in range(n):
        stamp = stamps[i]
        stamps_set.add(stamp)
    return len(stamp_set)

n = int(input().strip())
stamps = []
for i in range(n):
    stamps.append(input().strip())
    
print(count_distinct_stamps(n, stamps))


