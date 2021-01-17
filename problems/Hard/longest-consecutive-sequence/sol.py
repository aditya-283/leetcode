from typing import List


class Solution:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0
		nums = list(set(nums))
		nums.sort()
		consec = [0] * len(nums)
		for i, num in enumerate(nums):
			if num == nums[i-1] + 1:
				consec[i] = 1

		max_count, count = 0, 0
		for x in consec:
			if x == 1:
				count += 1
				max_count = max(max_count, count)
			else:
				count = 0
		print(nums, consec, max_count)
		return max_count + 1

print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive([1,2,0,1]))

