# problem link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


# Description:
"""
You are given an array of integers nums and the head of a linked list. Return the head of the modified linked list after removing all nodes from the linked list that have a value that exists in nums.

 

Example 1:

Input: nums = [1,2,3], head = [1,2,3,4,5]

Output: [4,5]

Explanation:



Remove the nodes with values 1, 2, and 3.

Example 2:

Input: nums = [1], head = [1,2,1,2,1,2]

Output: [2,2,2]

Explanation:



Remove the nodes with value 1.

Example 3:

Input: nums = [5], head = [1,2,3,4]

Output: [1,2,3,4]

Explanation:



No node has value 5.
"""

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # Convert the nums list into a set for faster lookup
        nums_set = set(nums)
        
        # Create a dummy node to simplify edge cases such as removing the head node
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        # Traverse the linked list
        while current and current.next:
            if current.next.val in nums_set:
                # Skip the node with value in nums
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the head of the modified list
        return dummy.next