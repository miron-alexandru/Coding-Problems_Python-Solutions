# problem link: https://leetcode.com/problems/maximum-average-pass-ratio/


# my solution:
import heapq

class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:   
        # calculate the potential increase in pass ration
        def delta(passi, totali):
            return (passi + 1) / (totali + 1) - passi / totali
        # Max-heap (store -delta for max-heap simulation)
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-delta(passi, totali), passi, totali))
        #assign each student
        for i in range(extraStudents):
            d, passi, totali = heapq.heappop(heap)
            passi += 1
            totali += 1
            heapq.heappush(heap, (-delta(passi, totali), passi, totali))

        total_ratio = sum(passi / totali for _, passi, totali in heap)
        return total_ratio / len(classes)
