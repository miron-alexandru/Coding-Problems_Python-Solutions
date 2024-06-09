# problem link: https://leetcode.com/problems/subarray-sums-divisible-by-k


# my solution:
class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        # Initialize the dictionary to count remainders
        remainder_count = {0: 1}
        # Initialize the count of valid subarrays
        count = 0

        for i in range(len(nums)):
            # Update the prefix sum with the current number
            prefix_sum += nums[i]
            # Compute the remainder of the current prefix sum when divided by k
            remainder = prefix_sum % k

            # Adjust the negatives to non-negatives
            if remainder < 0:
                remainder += k

            # Get the count of subarrays seen with this remainder
            count_of_remainder = remainder_count.get(remainder, 0)
            # Add this count to the total count of valid subarrays
            count += count_of_remainder

            # Update the remainder_count dictionary with the current remainder
            if remainder in remainder_count:
                remainder_count[remainder] += 1
            else:
                remainder_count[remainder] = 1

        return count
