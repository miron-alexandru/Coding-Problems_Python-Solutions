# Problem Link: https://www.hackerrank.com/challenges/30-queues-stacks/problem


# My Solution:

from collections import deque


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = deque()

    def pushCharacter(self, ch):
        self.stack.append(ch)

    def enqueueCharacter(self, ch):
        self.queue.append(ch)

    def popCharacter(self):
        return self.stack.pop()

    def dequeueCharacter(self):
        return self.queue.popleft()
