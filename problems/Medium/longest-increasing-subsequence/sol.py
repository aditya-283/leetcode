from typing import List
from bisect import bisect_left

class Solution:
	def lengthOfLIS(self, nums: List[int]) -> int:
		n = len(nums)
		dp = [1]*n
		for i in range(n):
			for j in range(i):
				if nums[j] < nums[i]:
					dp[i] = max(dp[i], dp[j] + 1)
		return max(dp)
			



print(Solution().lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))