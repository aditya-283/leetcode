from typing import List
from itertools import accumulate


class Solution:
	def checkSubarraySum(self, nums: List[int], k: int) -> bool:
		existsKMultiplePair = any((i, j) for i, j in zip(nums, nums[1:]) if i % k == 0 and j % k == 0)
		c_sums = list(accumulate([num for num in nums if num % k]))
		c_mods = [x % k for x in c_sums]
		return existsKMultiplePair or (len(set(c_mods)) < len(c_sums)) or (0 in c_mods)


print(Solution().checkSubarraySum([5,0,0,0], 3))