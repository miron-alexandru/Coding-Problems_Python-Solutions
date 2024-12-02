# problem link: https://leetcode.com/problems/check-if-n-and-its-double-exist/


# my solutions:
# Brute force:
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i != j and arr[i] == 2 * arr[j]:
                    return True
        return False


# Set solution:
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()

        for i in arr:
            if i / 2 in seen:
                return True
            if 2 * i in seen:
                return True

            seen.add(i)

        return False