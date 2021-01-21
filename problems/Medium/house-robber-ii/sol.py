
from typing import List
from functools import cache

class Solution:
	def rob(self, nums):
		l = len(nums)
		@cache
		def robHelper(i, j):
			if i > j:
				return 0
			return max(nums[i] + robHelper(i+2, j), robHelper(i+1, j))

		return max(nums[0] + robHelper(2, l-2), robHelper(1, l-1))


print(Solution().rob([1, 2, 3 ,1]))