# problem link: https://leetcode.com/problems/reverse-linked-list/


# My Solution:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev

        return head