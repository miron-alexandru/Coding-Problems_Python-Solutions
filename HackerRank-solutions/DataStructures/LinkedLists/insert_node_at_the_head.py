# problem link: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem


# my solution:
def insertNodeAtHead(llist, data):
    new_node = SinglyLinkedListNode(data)
    if llist is None:
        return new_node
    else:
        new_node.next = llist
        return new_node
