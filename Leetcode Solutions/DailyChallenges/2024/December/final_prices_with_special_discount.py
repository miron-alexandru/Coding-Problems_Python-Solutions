# problem link: https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/


# my solution (brute-force):
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = []

        for i in range(len(prices)):
            discount = 0
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    discount = prices[j]
                    break
            answer.append(prices[i] - discount)

        return answer



# optimized solution:
class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answer = prices[:]
        stack = []

        for i, price in enumerate(prices):
        	# While the stack is not empty and the current price is less than or equal to the price at stack's top
            while stack and prices[stack[-1]] >= price:
            	# Pop the index from the stack
                j = stack.pop()
                # Apply the discount
                answer[j] = prices[j] - price
            # Push the current index onto the stack
            stack.append(i)

        return answer