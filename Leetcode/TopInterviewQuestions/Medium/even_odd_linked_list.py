# problem link: https://leetcode.com/problems/odd-even-linked-list/


# my solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        # separate odd and even nodes into separate lists
        odd_head, even_head = head, head.next
        odd_tail, even_tail = odd_head, even_head
        curr = even_head.next
        index = 3

        while curr:
            if index % 2 == 1:  # odd index
                odd_tail.next = curr
                odd_tail = curr
            else:  # even index
                even_tail.next = curr
                even_tail = curr
            curr = curr.next
            index += 1

        # link odd and even lists
        odd_tail.next = even_head
        even_tail.next = None

        return odd_head
