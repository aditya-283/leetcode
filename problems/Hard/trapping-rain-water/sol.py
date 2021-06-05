from typing import List
from collections import deque
from itertools import accumulate

class Solution:
	def trap(self, height: List[int]) -> int:
		lmax = list(accumulate(height, max))
		rmax = list(reversed(list(accumulate(reversed(height), max))))
		return sum(min(lmax[i], rmax[i]) - height[i] for i in range(len(height)))

print(Solution().trap(height = 
[6, 8, 5, 0, 0, 6, 5]))