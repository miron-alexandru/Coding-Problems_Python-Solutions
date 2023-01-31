# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. 
# For example, alison heck should be capitalised correctly as Alison Heck.
# Given a full name, your task is to capitalize the name appropriately.


# Input format
# A single line of input containing the full name, S.

# Output Format
# Print the capitalized string, S.


# Sample Input
# chris alan


# Sample Output
# Chris Alan


# My Solution
def solve(s):
    for i in s.split():
        s = s.replace(i,i.capitalize())
    return s

