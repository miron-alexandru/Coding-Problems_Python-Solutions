# problem link: https://leetcode.com/problems/find-unique-binary-string/



# my solution:
def findDifferentBinaryString(nums):
	# Construct a new binary string by flipping the i-th bit of nums[i]
    return ''.join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
