# problem link: https://www.hackerrank.com/challenges/delete-a-node-from-a-linked-list/problem

# my solution:
def deleteNode(llist, position):
    if llist is None:  # list is empty
        return None
    elif position == 0:  # delete head node
        llist = llist.next
        return llist
    else:  # delete node at given position
        current = llist
        prev = None
        index = 0
        while current is not None and index < position:
            prev = current
            current = current.next
            index += 1
        if current is None:  # position is out of range
            return llist
        prev.next = current.next
        return llist
