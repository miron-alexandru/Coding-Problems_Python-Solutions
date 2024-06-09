# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy node to handle edge cases
        dummy = ListNode(0)
        dummy.next = head
        fast = dummy
        slow = dummy

        # Move fast pointer n nodes ahead
        for _ in range(n + 1):
            fast = fast.next

        # Move both pointers until the fast pointer reaches the end
        while fast is not None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next

        return dummy.next
