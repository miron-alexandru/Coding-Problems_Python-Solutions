# problem link: https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits



# my solutions:

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
       return sorted(arr, key=lambda x: (bin(x).count('1'), x))



class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def count_bits(num):
            count = 0
            while num:
                count += num & 1
                num >>= 1
            return count
            
        def custom_sort(item):
            return (count_bits(item), item)

        return sorted(arr, key=custom_sort)