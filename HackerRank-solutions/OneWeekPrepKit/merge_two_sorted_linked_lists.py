# Problem Link; https://www.hackerrank.com/challenges/one-week-preparation-kit-merge-two-sorted-linked-lists/problem


# My Solution:
def mergeLists(headA, headB):
    if not headA:
        return headB
    elif not headB:
        return headA

    merged_head = SinglyLinkedListNode(None)
    current = merged_head

    while headA and headB:
        if headA.data < headB.data:
            current.next = headA
            headA = headA.next
        else:
            current.next = headB
            headB = headB.next
        current = current.next

    if headA:
        current.next = headA
    elif headB:
        current.next = headB

    return merged_head.next
