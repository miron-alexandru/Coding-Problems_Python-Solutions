# problem link: https://leetcode.com/problems/partition-list


# my solution:

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # node for the partition with nodes less than x
        less_head = ListNode()
        # node for the partition with nodes greater than or equal to x
        greater_head = ListNode()
        # Pointer to the end of the less partition
        less_tail = less_head
        # Pointer to the end of the greater partition
        greater_tail = greater_head
        
        # Traverse the original linked list
        current = head
        while current:
            if current.val < x:
                # Append the current node to the less partition
                less_tail.next = current
                # Move the less_tail pointer to the new end
                less_tail = less_tail.next
            else:
                # Append the current node to the greater partition
                greater_tail.next = current
                # Move the greater_tail pointer to the new end
                greater_tail = greater_tail.next
            # Move to the next node
            current = current.next
        
        # Connect the two partitions
        # Connect the end of less partition to the start of greater partition
        less_tail.next = greater_head.next
        # Mark the end of the greater partition
        greater_tail.next = None
        
        return less_head.next