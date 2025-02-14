# problem link: https://leetcode.com/problems/product-of-the-last-k-numbers/



# solution:
class ProductOfNumbers:
    def __init__(self):
        self.prefix_products = [1]  # Initialize with 1 to handle multiplication cases
        self.zero_index = -1  # Keeps track of the last zero's index

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix_products = [1]  # Reset because a zero invalidates previous products
            self.zero_index = len(self.prefix_products) - 1
        else:
            self.prefix_products.append(self.prefix_products[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.prefix_products):
            return 0  # If k extends beyond the last zero, return 0
        return self.prefix_products[-1] // self.prefix_products[-(k+1)]

        

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)