# problem link: https://leetcode.com/problems/letter-combinations-of-a-phone-number


# my solutions:
# recursive
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # mapping of digits to letters
        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def track(combination, next_digits):
            if not next_digits:
                output.append(combination)
            else:
                for letter in digitsToLetters[next_digits[0]]:
                	# recursively call track with updated combination and next_digits substring
                    track(combination + letter, next_digits[1:])
        output = []
        track("", digits)
        return output


# iterative

from collections import deque

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        digitsToLetters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # Initialize a queue with an empty string
        queue = deque([""])

        for digit in digits:
            # Get the letters corresponding to the current digit
            letters = digitsToLetters[digit]
            
            # For each existing combination in the queue, append each letter
            # from the current digit's letters to create new combinations
            size = len(queue)
            for _ in range(size):
                current_combination = queue.popleft()
                for letter in letters:
                    queue.append(current_combination + letter)

        return list(queue)
