# problem link: https://leetcode.com/problems/merge-two-sorted-lists


# my solution:


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head_merge = ListNode(None)
        node = head_merge
        p1 = list1
        p2 = list2

        while p1 is not None and p2 is not None:
            if p1.val <= p2.val:
                node.next = ListNode(p1.val)
                p1 = p1.next
            else:
                node.next = ListNode(p2.val)
                p2 = p2.next
            node = node.next

        if p1 is not None:
            node.next = p1
        elif p2 is not None:
            node.next = p2

        return head_merge.next
