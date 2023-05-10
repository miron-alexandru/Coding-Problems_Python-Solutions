# problem link: https://leetcode.com/problems/linked-list-cycle-ii


# my solutionn:
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        # traverse with fast moving twice as fast as slow
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # if cycle is found init a new pointer
            if fast == slow:
                pointer = head
                # traverse with new pointer and slow moving at the same time
                while pointer != slow:
                    pointer = pointer.next
                    slow = slow.next
                # the cycle begins when they meet
                return pointer
        # no cycle
        return None
