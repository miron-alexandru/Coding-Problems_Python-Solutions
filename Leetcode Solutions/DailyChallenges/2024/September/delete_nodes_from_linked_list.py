# problem link: https://leetcode.com/problems/delete-nodes-from-linked-list-present-in-array/


# my solution:
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