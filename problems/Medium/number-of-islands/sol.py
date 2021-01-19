from typing import List
from collections import deque, defaultdict

class Solution:
	def numIslands(self, grid: List[List[str]]) -> int:
		R = len(grid)
		C = len(grid[0])

		def dfs(r, c):
			if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == '0' or grid[r][c] == '2':
				return 0

			grid[r][c] = '2'
			dfs(r, c-1)
			dfs(r, c+1)
			dfs(r-1, c)
			dfs(r+1, c)

		islands = 0
		for i in range(R):
			for j in range(C):
				if grid[i][j] == '1':
					islands += 1
					dfs(i, j)
		return islands

print(Solution().numIslands( [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
))



# SIMPLIFY CODE. All medium problems are such that they can be pondered over, and solved correctly with working code that respects all edge cases corner cases in 20 MINUTES MAX. 
# If that isn't happening, your code is too complex. SIMPLFY. No tuples. NEVER use itertools filter or map, its too expensive. 