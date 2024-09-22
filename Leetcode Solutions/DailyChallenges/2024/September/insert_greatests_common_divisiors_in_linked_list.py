# problem link: https://leetcode.com/problems/insert-greatest-common-divisors-in-linked-list/


# my solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current = head
        
        while current and current.next:
            # Find the GCD of the current node and the next node
            gcd_val = math.gcd(current.val, current.next.val)
            
            # Create a new node with the GCD value
            new_node = ListNode(val=gcd_val)
            
            # Insert the new node between current and current.next
            new_node.next = current.next
            current.next = new_node
            
            # Move current to the next pair (skip the newly inserted node)
            current = new_node.next
        
        return head