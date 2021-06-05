from typing import List
from functools import cache
from math import inf

class Solution:
	def lastStoneWeightII(self, stones: List[int]) -> int:
		@cache
		def rec(w, i):
			if i == len(stones):
				return abs(w)
			return min(rec(w + stones[i], i+1), rec(w - stones[i], i+1))
		return rec(0, 0)


print(Solution().lastStoneWeightII(stones = [89,23,100,93,82,98,91,85,33,95,72,98,63,46,17,91,92,72,77,79,99,96,55,72,24,98,79,93,88,92]))