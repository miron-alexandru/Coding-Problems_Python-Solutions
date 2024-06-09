# problem link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/


# my solution:
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
            "9": "wxyz",
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
