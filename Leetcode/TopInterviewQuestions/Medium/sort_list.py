# problem link: https://leetcode.com/problems/sort-list/


# my solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # base case:
        if not head or not head.next:
            return head

        # use fast and slow pointers
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Recursive call to sort the two halves
        right = self.sortList(slow.next)
        slow.next = None
        left = self.sortList(head)

        # Merge the two sorted halves
        merged = ListNode()
        tail = merged
        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left or right

        # Return the head of the sorted linked list
        return merged.next
