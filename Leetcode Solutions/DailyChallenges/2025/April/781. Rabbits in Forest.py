# problem link: https://leetcode.com/problems/rabbits-in-forest/description/


# Description
"""
There is a forest with an unknown number of rabbits. We asked n rabbits "How many rabbits have the same color as you?" and collected the answers in an integer array answers where answers[i] is the answer of the ith rabbit.

Given the array answers, return the minimum number of rabbits that could be in the forest.

 

Example 1:

Input: answers = [1,1,2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit that answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.
Example 2:

Input: answers = [10,10,10]
Output: 11
 

Constraints:

1 <= answers.length <= 1000
0 <= answers[i] < 1000
"""

# Solution:
class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # Count how many rabbits gave each answer
        count = Counter(answers)
        total = 0

        # Loop through each unique answer x
        for x in count:
            group_size = x + 1  # Each rabbit saying 'x' implies a group of x + 1 rabbits
            num_rabbits = count[x]  # How many rabbits gave this answer

            # Calculate how many full groups we need
            # - using ceiling division to make sure no rabbit is left unaccounted
            num_groups = (num_rabbits + group_size - 1) // group_size

            # Each group contributes group_size rabbits
            total += num_groups * group_size

        return total