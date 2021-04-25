from typing import List

class Solution:
	def majorityElement(self, nums: List[int]) -> int:
		x = nums[0]
		count = 1
		for num in nums:
			if num == x:
				count += 1
			else:
				count -= 1

			if count == 0:
				x = num
				count = 1
		return x if nums.count(x) > len(nums) // 2 else -1
				

print(Solution().majorityElement([2,2,1,1,1,2,2]))