# problem link: https://leetcode.com/problems/swapping-nodes-in-a-linked-list/


# my solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Traverse the linked list to find the length
        length = 0
        curr = head
        while curr:
            curr = curr.next
            length += 1

        # Check if k is valid
        if k < 1 or k > length:
            return head

        # Initialize pointers
        first = head
        second = head
        prev_second = None

        # Traverse to the kth node from the beginning
        for _ in range(k - 1):
            first = first.next

        # Traverse to the kth node from the end
        for _ in range(length - k):
            prev_second = second
            second = second.next

        # Swap the values of the first and second nodes
        first.val, second.val = second.val, first.val

        return head