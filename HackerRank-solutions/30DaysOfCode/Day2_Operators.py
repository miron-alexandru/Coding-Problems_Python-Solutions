'''
Given the meal price (base cost of a meal), tip percent
(the percentage of the meal price being added as tip), and tax
percent (the percentage of the meal price being added as tax)
for a meal, find and print the meal's total cost. Round the result 
to the nearest integer.


Function Description
Complete the solve function in the editor below.

solve has the following parameters:
int meal_cosT: the cost of food before tip and tax.
int tip_percent: the tip percentage
int tax_percent: the tax percentage

Returns: The function returns nothing. Print the calculated value,
rounded to the nearset integer.


Input format
There are 3 lines of numeric input:
The first line has a double, meal cost
The second line has an integer, tip percent
The third line has an integer, tax percent

Sample Input
12.00
20
8

Sample output
15
'''

# My solution:
def solve(meal_cost, tip_percent, tax_percent):
    tip_cost = meal_cost / 100 * tip_percent
    tax_cost = tax_percent / 100 * meal_cost
    total_cost = meal_cost + tip_cost + tax_cost
    print(round(total_cost))
if __name__ == '__main__':
    meal_cost = float(input().strip())

    tip_percent = int(input().strip())

    tax_percent = int(input().strip())

    solve(meal_cost, tip_percent, tax_percent)
