from typing import List
from bisect import bisect_left

class Solution:
	def maxDistance(self, position: List[int], m: int) -> int:
		n = len(position)
		position.sort()
		def isPossible(d):
			last = position[0]
			for i in range(m-1):
				idx = bisect_left(position, last + d)
				if (idx >= n):
					return False
				last = position[idx]
			return True

		lower = min(nxt - prev for prev, nxt in zip(position, position[1:]))
		upper = (position[-1] - position[0])//(m - 1)
		cand = upper
		while True:
			if isPossible(cand):
				lower = cand
			else:
				upper = cand
			cand = (lower + upper)//2
			if cand == lower:
				break
		return lower


print(Solution().maxDistance(position = [5,4,3,2,1,1000000000], m = 2))