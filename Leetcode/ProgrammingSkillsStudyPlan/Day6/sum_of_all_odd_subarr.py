# problem link: https://leetcode.com/problems/sum-of-all-odd-length-subarrays


# my solution:
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Get the length of the input array
        n = len(arr)
        
        # Init odd_sum to 0
        odd_sum = 0
        
        # Loop over all starting indices i
        for i in range(n):
            # Loop over all possible odd length subarr starting at index i
            for j in range(1, n-i+1, 2):
                # Get the subarr from index i to i+j
                subarr = arr[i:i+j]
                
                # Add the sum of the subarr to the total odd_sum
                odd_sum += sum(subarr)
        
        # Return odd_sum
        return odd_sum
