# Problem Link: https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/problem


# My Solution:
class Queue:
    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, value):
        self.enqueue_stack.append(value)

    def dequeue(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("empty queue")
        self.dequeue_stack.pop()

    def front(self):
        if not self.dequeue_stack:
            while self.enqueue_stack:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        if not self.dequeue_stack:
            raise IndexError("empty queue")
        return self.dequeue_stack[-1]


queue = Queue()

q = int(input())
for i in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        queue.enqueue(query[1])
    elif query[0] == 2:
        queue.dequeue()
    elif query[0] == 3:
        print(queue.front())
