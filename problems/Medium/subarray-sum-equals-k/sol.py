from typing import List
from itertools import accumulate
from collections import defaultdict

class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:
		result, sum_, hashmap = 0, 0, defaultdict(int)
		hashmap[0] = 1
		for num in nums:
			sum_ += num
			if sum_ - k in hashmap:
				result += hashmap[sum_ - k]
			hashmap[sum_] += 1
		return result
print(Solution().subarraySum([1,2,3], 3))