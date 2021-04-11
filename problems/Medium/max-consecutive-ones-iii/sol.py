from typing import List

class Solution:
	def longestOnes(self, nums: List[int], k: int) -> int:
		maxLen = 0
		start, end = 0, 0
		flipped = 0
		while end < len(nums):
			if nums[end] == 0 and flipped < k:
				flipped += 1
				end += 1
			elif nums[end] == 1:
				end += 1
			elif nums[end] == 0 and flipped >= k:
				if nums[start] == 0:
					flipped -= 1
				start += 1
			maxLen = max(maxLen, end - start)
		return maxLen

print(Solution().longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))



