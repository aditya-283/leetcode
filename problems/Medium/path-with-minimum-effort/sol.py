from typing import List
from heapq import heappush, heappop
from math import inf

class Solution:
	def minimumEffortPath(self, heights: List[List[int]]) -> int:
		R, C = len(heights), len(heights[0])
		distances = [[inf]*C for _ in range(R)]
		heap= [(0, 0, 0)]
		distances[0][0] = 0
		while heap:
			d, i, j= heappop(heap)
			nbrs = ((i+1, j), (i-1, j), (i, j+1), (i, j-1))
			for r, c in nbrs:
				if 0 <= r < R and 0 <= c < C and max(d, abs(heights[r][c] - heights[i][j])) < distances[r][c]:
					distances[r][c] = max(d, abs(heights[r][c] - heights[i][j]))
					heappush(heap, (distances[r][c], r, c))
		return distances[R-1][C-1]



