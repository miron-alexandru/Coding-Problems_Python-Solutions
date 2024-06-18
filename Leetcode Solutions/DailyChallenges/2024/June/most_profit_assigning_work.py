# problem link: https://leetcode.com/problems/most-profit-assigning-work/


# my solution:
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # Combine difficulty and profit into tuples and sort them by difficulty primary and profit secondary, descending
        jobs = sorted(zip(difficulty, profit), key=lambda x: (x[0], -x[1]))
        worker.sort()

        max_profit = 0
        total_profit = 0
        job_index = 0
        n = len(jobs)
        
        for ability in worker:
            # While the current job's difficulty is less than or equal to the worker's ability
            while job_index < n and jobs[job_index][0] <= ability:
                # Update max_profit if the current job's profit is higher
                max_profit = max(max_profit, jobs[job_index][1])
                # next job
                job_index += 1
            # Add the best available job profit for this worker to total_profit
            total_profit += max_profit
        
        return total_profit