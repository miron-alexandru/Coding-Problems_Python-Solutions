# problem link: https://www.hackerrank.com/challenges/insertionsort1/problem


# my solution:
def insertionSort1(n, arr):
    # Store value of the unsorted element
    val = arr[n - 1]

    # set index to the second last element in the array
    j = n - 2

    while j >= 0 and arr[j] > val:
        # shift the elements that are greater than the unsorted element to the right
        arr[j + 1] = arr[j]
        # Decrement the index
        j -= 1
        # print after each shift
        print(" ".join(map(str, arr)))

    # insert the unsorted element into the correct position
    arr[j + 1] = val

    # print sorted array
    print(" ".join(map(str, arr)))
