from typing import List
from functools import cache

class Solution:
	def rob(self, nums: List[int]) -> int:
		@cache
		def robHelper(i, till):
			if i >= till:
				return 0
			return max(nums[i] + robHelper(i+2, till), robHelper(i+1, till))

		if len(nums) == 0:
			return 0
		elif len(nums) <= 3:
			return max(nums)
		return max(nums[0] + robHelper(2, len(nums)-1), \
					robHelper(1, len(nums)))

print(Solution().rob([1, 2, 3, 4, 5, 1, 2, 3, 4, 5]))