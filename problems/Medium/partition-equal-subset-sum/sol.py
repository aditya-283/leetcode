from typing import List
from functools import cache

class Solution:
	def canPartition(self, nums: List[int]) -> bool:
		n = len(nums)
		@cache
		def isSubsetSum(sum, i):
			if i >= n:
				return False
			if sum == 0:
				return True
			else:
				return isSubsetSum(sum - nums[i], i+1) or isSubsetSum(sum, i+1)

		if sum(nums)%2:
			return False
		else:
			return isSubsetSum(sum(nums) // 2, 0)

print(Solution().canPartition([1,2,3,5]))