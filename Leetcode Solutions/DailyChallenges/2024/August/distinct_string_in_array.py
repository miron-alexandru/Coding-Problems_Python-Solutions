# problem link: https://leetcode.com/problems/kth-distinct-string-in-an-array/


# my solution:

# First solution
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = {}
        distinct_list = []

        for i in arr:
            if i in count_dict:
                count_dict[i] += 1
            else:
                count_dict[i] = 1
    
        for j in arr:
            if count_dict[j] == 1:
                distinct_list.append(j)

        if len(distinct_list) >= k:
            return distinct_list[k-1]

        return ""


# Second Solution:
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        count_dict = Counter(arr)

        distinct_list = [s for s in arr if count_dict[s] == 1]

        return distinct_list[k-1] if k <= len(distinct_list) else ""