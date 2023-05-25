# problem link: https://www.hackerrank.com/challenges/insertionsort2/problem


# my solution:
def insertionSort2(n, arr):
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted
        j = i - 1  # Index of the previous element

        # Shift elements greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key  # Insert the current element at its correct position
        print(" ".join(map(str, arr)))
