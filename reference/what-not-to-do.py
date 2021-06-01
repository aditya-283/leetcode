from typing import List
from functools import cache
from operator import itemgetter
from bisect import bisect_left

class Envelope:
	def __init__(self, l):
		self.env = tuple(l)

	def __eq__(self, other):
		return self.env[0] == other.env[0] or self.env[1] == other.env[1]

	def __lt__(self, other):
		return self.env[0] < other.env[0] and self.env[1] < other.env[1]

	def __gt__(self, other):
		return self.env[0] > other.env[0] and self.env[1] > other.env[1]

	def __repr__(self):
		return f'{self.env}'

# LOOK AT THE HOURS OF WASTED EFFORT TRYING TO MAKE ORDERED WHAT IS BY DEFINITION UNORDERABLE. 
# NO DEFINITION OR INGENUITY CAN HELP YOU DO BINARY SEARCH OVER ENVELOPES, THERE WILL EITHER
	## EXIST PAIRS FOR WHICH NONE OF LT GT OR EQ RELATIONS HOLDS
	## EXIST INCONSISTENT COMPARISONS - C < D; A = C, A = D
class Solution:
	def lengthOfLIS(self, nums) -> int:
		tops = []
		envs = [Envelope(num) for num in nums]
		print(envs)
		for num in envs:
			idx = bisect_left(tops, num)
			if idx == len(tops):
				tops.append(num)
			else:
				tops[idx] = Envelope(min(tops[idx].env, num.env))

		print(tops)
		ans = []
		for top in tops:
			if not ans or top > ans[-1]:
				ans.append(top)
		return len(ans)
		

	def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
		envelopes.sort(key=itemgetter(0))
		return self.lengthOfLIS(envelopes)

print(Solution().maxEnvelopes(envelopes = [[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))