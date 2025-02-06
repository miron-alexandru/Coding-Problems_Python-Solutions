# problem link: https://leetcode.com/problems/tuple-with-same-product/



# my solution:
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        product_map = defaultdict(list)

        for i in range(n):
            for j in range(i + 1, n):
                product = nums[i] * nums[j]
                product_map[product].append((i, j))

        for product, pairs in product_map.items():
            pair_count = len(pairs)
            if pair_count >= 2:
                count += (pair_count * (pair_count - 1)) // 2 * 8

        return count