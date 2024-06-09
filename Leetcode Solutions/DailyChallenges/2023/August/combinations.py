# problem link: https://leetcode.com/problems/combinations


# my solution:
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # Define a recursive function to generate combinations
        def backtrack(start, current_combination):
            # Base case: if the current combination is of size k add it to the result list
            if len(current_combination) == k:
                result.append(current_combination[:])
                return

            # Explore all possibilities
            for i in range(start, n + 1):
                # Make a decision to include the current number in the combination
                current_combination.append(i)

                # move to the next position and explore further
                backtrack(i + 1, current_combination)

                # remove the last added number to try other possibilities
                current_combination.pop()

        # empty list to store the result combinations
        result = []

        # Start the backtracking with an empty combination and index 1
        backtrack(1, [])

        return result
