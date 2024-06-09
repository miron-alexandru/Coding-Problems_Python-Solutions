# problem link: https://leetcode.com/problems/add-two-numbers


# my solution:

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        carry = 0
        result_head = ListNode()
        current_node = result_head

        while l1 or l2 or carry:
            sum = carry

            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry = sum // 10
            sum %= 10

            current_node.next = ListNode(sum)
            current_node = current_node.next

        return result_head.next