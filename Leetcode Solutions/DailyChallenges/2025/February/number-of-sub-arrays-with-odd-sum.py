# problem link: https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/



# my solution:
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # even_count starts at 1 because the initial prefix sum is 0 (even)
        # odd_count starts at 0 since no odd prefix sum has been encountered yet
        even_count = 1
        odd_count = 0
        result = 0

        prefix_sum = 0
        for num in arr:
            prefix_sum += num  # Update the prefix sum with the current element

            # Check if the prefix sum is even or odd
            if prefix_sum % 2 == 0:
                # If the current prefix sum is even add the count of odd prefix sums to result
                result += odd_count
                even_count += 1  # Increment the count of even prefix sums
            else:
                # If the current prefix sum is odd add the count of even prefix sums to result
                result += even_count
                odd_count += 1  # Increment the count of odd prefix sums

        result %= 10**9 + 7

        return result
