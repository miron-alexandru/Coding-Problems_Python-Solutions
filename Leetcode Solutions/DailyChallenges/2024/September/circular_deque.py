# problem link: https://leetcode.com/problems/design-circular-deque/


# my solution:
class MyCircularDeque:

    def __init__(self, k: int):
        """
        Initialize the deque with a fixed size of k.
        """
        self.k = k
        self.deque = [0] * k  # Allocate memory for the deque
        self.front = 0        # Pointer to the front
        self.rear = 0         # Pointer to the rear
        self.size = 0         # Current number of elements in the deque

    def insertFront(self, value: int) -> bool:
        """
        Adds an item at the front of Deque.
        """
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.k  # Move front pointer backward in a circular manner
        self.deque[self.front] = value
        self.size += 1
        return True

    def insertLast(self, value: int) -> bool:
        """
        Adds an item at the rear of Deque.
        """
        if self.isFull():
            return False
        self.deque[self.rear] = value
        self.rear = (self.rear + 1) % self.k  # Move rear pointer forward in a circular manner
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        """
        Deletes an item from the front of Deque.
        """
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.k  # Move front pointer forward in a circular manner
        self.size -= 1
        return True

    def deleteLast(self) -> bool:
        """
        Deletes an item from the rear of Deque.
        """
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.k  # Move rear pointer backward in a circular manner
        self.size -= 1
        return True

    def getFront(self) -> int:
        """
        Returns the front item from the Deque. If the deque is empty, returns -1.
        """
        if self.isEmpty():
            return -1
        return self.deque[self.front]

    def getRear(self) -> int:
        """
        Returns the last item from the Deque. If the deque is empty, returns -1.
        """
        if self.isEmpty():
            return -1
        return self.deque[(self.rear - 1) % self.k]  # Rear points to the next insertion spot, so we get the previous element

    def isEmpty(self) -> bool:
        """
        Checks whether the deque is empty.
        """
        return self.size == 0

    def isFull(self) -> bool:
        """
        Checks whether the deque is full.
        """
        return self.size == self.k



# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()