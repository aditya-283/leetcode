from typing import List
from collections import deque
from itertools import product

class Solution:
	def closedIsland(self, grid: List[List[int]]) -> int:
		R, C = len(grid), len(grid[0])
		visited = set()

		def nbrs(i, j):
			return [(r, c) for r, c in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)) if 0 <= r < R and 0 <= c < C and grid[r][c] == 0]

		def bfs(s):
			q = deque([s])
			visited.add(s)
			while q:
				cur = q.pop()
				for nbr in nbrs(*cur):
					if nbr not in visited:
						visited.add(nbr)
						q.appendleft(nbr)
			return

		startingPoints = list(product(range(R), [0, C-1])) + list(product([0, R-1], range(C)))
		for r, c in startingPoints:
			if (r, c) not in visited and grid[r][c] == 0:
				bfs((r, c))

		count = 0
		for r, c in product(range(R), range(C)):
			if (r, c) not in visited and grid[r][c] == 0:
				bfs((r, c))
				count += 1
		return count

print(Solution().closedIsland(grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]))