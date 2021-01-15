from typing import List
import bisect

class Solution:
	def threeSum(self, nums: List[int]) -> List[List[int]]:
		uniqueSums = []
		nums.sort()
		for i in range(len(nums)):
			for j in reversed(range(len(nums))):
				if i == j:
					break

				if i > 0 and nums[i] == nums[i-1]:
					continue

				if j < len(nums)-1 and nums[j] == nums[j+1]:
					continue

				x, y, sum = nums[i], nums[j], -1*(nums[i]+nums[j])
				idx = bisect.bisect_left(nums, sum, i+1, j)
				if idx < j and nums[idx] == sum:
					uniqueSums.append([x, sum, y])

		return uniqueSums

if __name__ == '__main__':
	sol = Solution()
	# a = [-1, 0, 1, 2, -1, -4]
	a = [0,0,0,0, 0 , 0 , 0 , 0]
	print('Ans: ', sol.threeSum(a))
