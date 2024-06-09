# Problem Link: https://leetcode.com/problems/palindrome-linked-list/

# My Solution:


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # empty or only one node
        if not head or not head.next:
            return True

        # find the middle node of
        # the slow pointer moves one step at a time, the fast pointet two steps
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half of the list
        prev, curr = None, slow
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        # compare the first half of the list with the second
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next

        return True
