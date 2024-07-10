# problem link: https://leetcode.com/problems/crawler-log-folder/


# my solution:
class Solution:
    def minOperations(self, logs: List[str]) -> int:
        counter = 0

        for operation in logs:
            if operation == "../":
                if counter:
                    counter -= 1
            elif operation != "./":
                counter += 1

        return counter