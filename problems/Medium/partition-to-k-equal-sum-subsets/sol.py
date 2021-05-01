from typing import List
from functools import cache
import operator

class Solution:
	def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
		@cache
		def partitionUtil(i, subsets):
			if i == len(nums):
				return True
			l = list(subsets)
			for j, rem in enumerate(l):
				if nums[i] <= rem:
					l[j] -= nums[i]
					if partitionUtil(i+1, tuple(l)):
						return True
					l[j] += nums[i]


		subsetSum = sum(nums) // k
		nums.sort(reverse=True)
		return partitionUtil(0, tuple([subsetSum]*k))

print(Solution().canPartitionKSubsets([3522,181,521,515,304,123,2512,312,922,407,146,1932,4037,2646,3871,269], 5))



def zipWith(f, iter1, iter2):
	return [f(x,y) for x, y in zip(iter1, iter2)]



