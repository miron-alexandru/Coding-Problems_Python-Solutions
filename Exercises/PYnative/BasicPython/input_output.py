import os


# number1 = int(input('Give me two numbers to multiply, first: '))
# number2 = int(input('Second: '))

# res = number1 * number2
# print('Result:', res)

print("Name", "Is", "James", sep="**")
print()

num = 8
print("%o" % num)
print()

num = 458.541315

formatted_num = "{:.2f}".format(num)
print(formatted_num)
print("%.2f" % num)
print()

numbers = []
# for i in range(0, 5):
# print("Enter number at location", i, ":")
# item = float(input())
# numbers.append(item)
# print("User List:", numbers)

with open("test.txt", "r") as fp:
    lines = fp.readlines()

with open("new_file.txt", "w") as fp:
    count = 0

    for line in lines:
        if count == 4:
            count += 1
            continue
        else:
            fp.write(line)
        count += 1

# name1, name2, name3 = input("Enter three names: ").split()
# print('Name1:', name1, '\nName2:', name2, '\nName3:', name3)

total_money = 1000
quantity = 3
price = 450

statement = "I have {1} dollars so I can buy {0} football for {2:.2f} dollars."
print(statement.format(quantity, total_money, price))

size = os.stat("test.txt").st_size
if size == 0:
    print("file is empty")
else:
    print("File is not empty")

with open("test.txt", "r") as fp:
    # read all lines from a file
    lines = fp.readlines()
    # get line number 3
    print(lines[2])
