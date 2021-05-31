from typing import List
from collections import deque
from itertools import product

class Solution:
	def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
		R, C = len(grid), len(grid[0])
		def nbrs(i, j):
			return ((r, c) for r, c in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)) if 0 <= r < R and 0 <= c < C and grid[r][c] == 1)

		def bfs(s):
			cnt = 1
			visited.add(s)
			q = deque([s])
			while q:
				cur = q.pop()
				for nbr in nbrs(*cur):
					if nbr not in visited:
						visited.add(nbr)
						q.appendleft(nbr)
						cnt += 1
			return cnt

		visited = set()
		return max(0, 0, *(bfs((r, c)) for r, c in product(range(R), range(C)) if (r, c) not in visited and grid[r][c] == 1))

print(Solution().maxAreaOfIsland(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]))