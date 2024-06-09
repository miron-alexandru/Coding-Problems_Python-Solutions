# problem link: https://leetcode.com/problems/find-the-duplicate-number


# my solution:
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
    	# we create two pointers
        slow = nums[0]
        fast = nums[0]
        # move slow pointer one step at a time, fast pointer two steps
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        first_pointer = nums[0]
        second_pointer = slow
        while first_pointer != second_pointer:
            first_pointer = nums[first_pointer]
            second_pointer = nums[second_pointer]

        return first_pointer