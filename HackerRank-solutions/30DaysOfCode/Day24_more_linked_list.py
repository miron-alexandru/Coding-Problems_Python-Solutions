# Problem Link: https://www.hackerrank.com/challenges/30-linked-list-deletion/problem

# My Solution:
def removeDuplicates(self,head):
    if head is None:
        return None
            
    seen = set()
    seen.add(head.data)
        
    current = head
    while current.next is not None:
        if current.next.data in seen:
            current.next = current.next.next
        else:
            seen.add(current.next.data)
            current = current.next
        
    return head
