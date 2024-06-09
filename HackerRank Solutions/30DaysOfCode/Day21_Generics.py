# Problem Link: https://www.hackerrank.com/challenges/30-generics/problem


# Solution (Java):

public static <T> void printArray(T[] arr) {
    for (T element : arr) {
        System.out.println(element);
    }
}


# Solution: Python
def printArray(arr):
    for element in arr:
        print(element)
