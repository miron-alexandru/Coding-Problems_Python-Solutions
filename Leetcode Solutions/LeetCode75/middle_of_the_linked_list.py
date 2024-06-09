# problem link: https://leetcode.com/problems/middle-of-the-linked-list


# my solution:
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # init two pointers
        middle = end = head

        # move end two steps for every one step that middle moves
        while end is not None and end.next is not None:
            middle = middle.next
            end = end.next.next

        return middle
