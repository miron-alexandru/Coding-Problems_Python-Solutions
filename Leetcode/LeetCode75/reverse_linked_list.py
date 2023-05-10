# problem link: https://leetcode.com/problems/reverse-linked-list


# my solution:
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init pointers
        prev, curr = None, head
        while curr is not None:
            # store next node
            next_node = curr.next
            # reverse the link from curr to prev
            curr.next = prev
            # advance prev to curr
            prev = curr
            # advance curr to the next node
            curr = next_node

        return prev
