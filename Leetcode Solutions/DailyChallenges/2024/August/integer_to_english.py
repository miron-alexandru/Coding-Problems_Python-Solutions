# problem link: https://leetcode.com/problems/integer-to-english-words/


# solution:
class Solution:
    def numberToWords(self, num: int) -> str:
        # Handle the special case when num is 0
        if num == 0:
            return "Zero"

        # Function to convert numbers 1 to 9 to words
        def one(num):
            switcher = {
                1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five",
                6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
            }
            return switcher.get(num, "")

        # Function to convert numbers from 10 to 19 to words
        def two_less_20(num):
            switcher = {
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen",
                15: "Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen"
            }
            return switcher.get(num, "")

        # Function to convert multiples of 10 (20, 30, ..., 90) to words
        def ten(num):
            switcher = {
                2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
                6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
            }
            return switcher.get(num, "")

        # Function to convert numbers from 1 to 99 to words
        def two(num):
            if not num:
                return ""
            elif num < 10:
                return one(num)  # Numbers less than 10
            elif num < 20:
                return two_less_20(num)  # Numbers between 10 and 19
            else:
                tenner, below_ten = divmod(num, 10)  # Split into tens and units
                return ten(tenner) + (" " + one(below_ten) if below_ten else "")

        # Function to convert numbers from 1 to 999 to words
        def three(num):
            hundred, below_hundred = divmod(num, 100)  # Split into hundreds and the rest
            if hundred and below_hundred:
                return one(hundred) + " Hundred " + two(below_hundred)
            elif not hundred and below_hundred:
                return two(below_hundred)
            elif hundred and not below_hundred:
                return one(hundred) + " Hundred"
            return ""

        # Extract billions, millions, thousands, and the remainder
        billion, num = divmod(num, 1_000_000_000)  # Extract billions
        million, num = divmod(num, 1_000_000)  # Extract millions
        thousand, num = divmod(num, 1_000)  # Extract thousands

        # Build the result string
        res = ""
        if billion:
            res += three(billion) + " Billion"
        if million:
            res += " " + three(million) + " Million" if res else three(million) + " Million"
        if thousand:
            res += " " + three(thousand) + " Thousand" if res else three(thousand) + " Thousand"
        if num:
            res += " " + three(num) if res else three(num)

        return res.strip()
