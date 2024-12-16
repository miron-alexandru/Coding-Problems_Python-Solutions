# problem link: https://leetcode.com/problems/maximum-beauty-of-an-array-after-applying-operation/


# my solution:
from collections import defaultdict

class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        events = defaultdict(int)

        for num in nums:
            events[num - k] += 1
            events[num + k + 1] -= 1

        sorted_events = sorted(events.items())

        max_beauty = 0
        current_sum = 0

        for _, delta in sorted_events:
            current_sum += delta
            max_beauty = max(max_beauty, current_sum)

        return max_beauty