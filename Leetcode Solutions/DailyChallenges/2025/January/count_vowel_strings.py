# problem link: https://leetcode.com/problems/count-vowel-strings-in-ranges/



# my solution:
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # Helper function to check if a string starts and ends with a vowel
        def is_vowel_string(s: str) -> bool:
            vowels = {'a', 'e', 'i', 'o', 'u'}
            return s[0] in vowels and s[-1] in vowels
        
        # Create a prefix sum array to store counts of vowel strings
        n = len(words)
        prefix_sum = [0] * (n + 1)
        
        # Populate the prefix sum array
        for i in range(n):
            prefix_sum[i + 1] = prefix_sum[i] + (1 if is_vowel_string(words[i]) else 0)
        
        # Process each query and compute the result
        result = []
        for li, ri in queries:
            # Use prefix sums to calculate the count of vowel strings
            result.append(prefix_sum[ri + 1] - prefix_sum[li])
        
        return result
