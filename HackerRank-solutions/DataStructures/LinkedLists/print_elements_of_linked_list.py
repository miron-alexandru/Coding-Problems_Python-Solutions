# problem link: https://www.hackerrank.com/challenges/print-the-elements-of-a-linked-list/problem


# my solution:
def printLinkedList(head):
    curr = head
    while curr is not None:
        print(curr.data)
        curr = curr.next
