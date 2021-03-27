from typing import List


class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		i, zeroAt = 0, -1
		while i < len(nums):
			if zeroAt == -1 and nums[i] == 0:
					zeroAt = i
			elif nums[i] != 0 and zeroAt >= 0:
				nums[zeroAt], nums[i] = nums[i], nums[zeroAt]
				zeroAt += 1
			i += 1
		return nums


print(Solution().moveZeroes([1, 0, 1]))