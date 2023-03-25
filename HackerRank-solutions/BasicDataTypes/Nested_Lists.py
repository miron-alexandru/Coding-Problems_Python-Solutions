# Given the names and grades for each student in a class of n students,
# store them in a nested list and print the name(s) of any student(s) having
# the second lowest grade.

# Input Format
# The first line contains an integer,n , the number of students.
# The 2n subsequent lines describe each student over 2 lines.
# The first line contains a student's name
# The second line contains their grade.


# Output Format
# Print the name(s) of any student(s) having the second lowest grade in.
# If there are multiple students, order their names alphabetically and print
# each one line on a new line


# Sample Input
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39


# Sample Output
# Berry
# Harry


# My Solution:
if __name__ == '__main__':
    students = []
    for i in range(int(input())):
        name = input()
        grade = float(input())
        students.append([name, grade])
        
    second_lowest = sorted(set([grade for name, grade in students]))[1]
    students = [name for name, grade in students if grade == second_lowest]
    students.sort()
    for name in students:
        print(name)
