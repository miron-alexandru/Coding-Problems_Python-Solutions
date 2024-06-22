# problem link: https://leetcode.com/problems/count-number-of-nice-subarrays


# my solution:
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        # Initialize the count map
        count_map = defaultdict(int)
        # Handle case where a subarray starts from the beginning of the array
        count_map[0] = 1
        
        # Initialize variables to keep track of the number of odd numbers and the count of nice subarrays
        odd_count = 0
        nice_subarrays = 0

        for num in nums:
            # If the current number is odd increment the odd_count
            if num % 2 != 0:
                odd_count += 1

            # Check if there is a prefix subarray with exactly odd_count - k odd numbers
            if (odd_count - k) in count_map:
                # If such a prefix subarray exists add its frequency to the count of nice subarrays
                nice_subarrays += count_map[odd_count - k]
            
            # Update the count map with the current odd_count
            count_map[odd_count] += 1

        return nice_subarrays