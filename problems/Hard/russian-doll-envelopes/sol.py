from typing import List
from functools import cache
from operator import itemgetter
from bisect import bisect_left

class Solution:
	def lengthOfLIS(self, nums) -> int:
		tops = []
		for num in nums:
			idx = bisect_left(tops, num)
			if idx == len(tops):
				tops.append(num)
			else:
				tops[idx] = num
		return len(tops)
		
	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		envelopes.sort(key=lambda x: (x[0], -x[1]))
		envelopes = [env[1] for env in envelopes]
		return self.lengthOfLIS(envelopes)

print(Solution().maxEnvelopes(envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))