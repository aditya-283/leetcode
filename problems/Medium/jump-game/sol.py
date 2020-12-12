from typing import List
from functools import lru_cache

class Solution:
	def canJump(self, nums: List[int]) -> bool:
		@lru_cache
		def canJumpRec(pos):
			if pos == len(nums)-1 or pos + nums[pos] >= len(nums)-1:
				return True
			else:
				return any([canJumpRec(new_pos) for new_pos in range(pos+1, min(pos+nums[pos]+1, len(nums)))])
		return canJumpRec(0)

	def canJumpBU(self, nums):
		answers = [False]*len(nums)
		for idx in range(len(nums)-1, -1, -1):
			if idx == len(nums)-1:
				answers[idx] = True
			else:
				for ahead in range(idx+1, min(idx + nums[idx] + 1, len(nums))):
					if answers[ahead] == True:
						answers[idx] = True
						break
		return answers[0]

# Above recursion + memoization or table filling solutions are still overkill and time
# consuming because we're computing more than is needed.

	def canJumpGreedy(self, nums):
		lastValid = len(nums) - 1
		for i in range(len(nums)-1, -1, -1):
			if i + nums[i] >= lastValid:
				lastValid = i

		return lastValid == 0

print(Solution().canJumpGreedy([2,3,1,1,4]))