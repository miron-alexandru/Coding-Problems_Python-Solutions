# Problem Link: https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1


# My Solution:
def snail(array):
    snail = []
    while array:
        snail += array.pop(0)
        if array and array[0]:
            for row in array:
                snail.append(row.pop())
        if array:
            snail += array.pop()[::-1]
        if array and array[0]:
            for row in array[::-1]:
                snail.append(row.pop(0))
    return snail
