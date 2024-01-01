# problem link: https://leetcode.com/problems/top-k-frequent-elements

# my solution:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = {}

        for num in nums:
            frequency[num] = frequency.get(num, 0) + 1
        
        sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        
        result = []
        for i in range(k):
            result.append(sorted_frequency[i][0])
        
        return result