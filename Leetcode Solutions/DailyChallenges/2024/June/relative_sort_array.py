# problem link: https://leetcode.com/problems/relative-sort-array/


# my solution:

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # Create a dictionary to map each element in arr2 to its index
        index_map = {value: i for i, value in enumerate(arr2)}

        # ordered will hold elements of arr1 that are present in arr2
        # not_ordered will hold elements of arr1 that are not in arr2
        ordered = []
        not_ordered = []

        for i in arr1:
            # If the element is in arr2 (exists in the index_map) add it to ordered
            if i in index_map:
                ordered.append(i)
            # If the element is not in arr2, add it to not_ordered
            else:
                not_ordered.append(i)

        # Sort the ordered list based on the order defined in arr2
        # The key for sorting is the index in arr2, obtained from the index_map
        ordered.sort(key=lambda x: index_map[x])
        not_ordered.sort()

        return ordered + not_ordered
