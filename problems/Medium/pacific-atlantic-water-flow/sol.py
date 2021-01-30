from typing import List
from functools import cache
import sys
from collections import defaultdict

class Solution:
	def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
		if not matrix:
			return []

		R, C = len(matrix), len(matrix[0])
		
		def nbrs(i, j):
			return [(r, c) for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= r < R and 0 <= c < C]

		def dfsVisit(i, j, visited):
			visited.add((i, j))
			for r, c in nbrs(i, j):
				if (r, c) not in visited and matrix[i][j] <= matrix[r][c]:
					dfsVisit(r, c, visited)
			visited.add((i, j))

		def visitPacific():
			visited = set()
			for j in range(C):
				if (0, j) not in visited:
					dfsVisit(0, j, visited)

			for i in range(R):
				if (i, 0) not in visited:
					dfsVisit(i, 0, visited)

			return visited

		def visitAtlantic():
			visited = set()
			for j in range(C):
				if (R-1, j) not in visited:
					dfsVisit(R-1, j, visited)

			for i in range(R):
				if (i, C-1) not in visited:
					dfsVisit(i, C-1, visited)

			return visited

		return list(visitAtlantic().intersection(visitPacific()))


print(Solution().pacificAtlantic([[1, 2, 2, 3, 5],
								  [3, 2, 3, 4, 4],
								  [2, 4, 5, 3, 1],
								  [6, 7, 1, 4, 5],
								  [5, 1, 1, 2, 4]]))
