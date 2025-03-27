# problem link: https://leetcode.com/problems/minimum-index-of-a-valid-split/



# solution:

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        most_frequent_element, total_count = Counter(nums).most_common(1)[0]
        left_count = 0
        
        for index, value in enumerate(nums, 1):
            if value == most_frequent_element:
                left_count += 1
                
                if left_count * 2 > index and (total_count - left_count) * 2 > len(nums) - index:
                    return index - 1
        
        return -1
