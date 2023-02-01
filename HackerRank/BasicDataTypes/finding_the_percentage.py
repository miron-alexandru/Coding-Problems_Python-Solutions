# The provided code stub will read in a dictionary containing key/value pairs
# of name:[marks] for a list of students. Print the average of the marks array
# for the student name provided, showing 2 places after the decimal.

# Input Format
# The first line contains the integer n, the number of students' records.
# The next n lines contain the names and marks obtained by a student, each
# value separated by a space. The final line contains query_name, the name
# of a student to query.


# Output Format
# Print one line: The average of the marks obtained by 	the particular
# student correct to 2 decimal places

# Sample Input
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

# Sample Output
# 56.00


# My Solution:;
def average_marks(dictionary, name):
    marks = dictionary[name]
    return format(sum(marks) / len(marks), '.2f')

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(average_marks(student_marks, query_name))
