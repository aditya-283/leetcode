from typing import List

class Solution:
	def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
		return sorted(points, key=lambda x: x[0]**2 + x[1]**2)[:k]

print(Solution().kClosest([[3,3],[5,-1],[-2,4]], 2))