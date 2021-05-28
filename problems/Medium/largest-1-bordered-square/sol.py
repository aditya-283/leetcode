from typing import List

class Solution:
	def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
		def isValid(i, j):
			return 0 <= i < n and 0 <= j < m

		n, m = len(grid), len(grid[0])
		rowAcc = [[0]*m for _ in range(n)]
		colAcc = [[0]*m for _ in range(n)]
		for i in range(n):
			for j in range(m):
				if grid[i][j]:
					rowAcc[i][j] = 1 + rowAcc[i][j-1] if j > 0 else 1 
					colAcc[i][j] = 1 + colAcc[i-1][j] if i > 0 else 1 
				else:
					rowAcc[i][j], colAcc[i][j] = 0, 0

		ans = 0
		for i in range(n):
			for j in range(m):
				for k in range(min(m, n)):
					if grid[i][j] and isValid(i+k, j+k) and \
					 	min(rowAcc[i][j+k], colAcc[i+k][j], rowAcc[i+k][j+k], colAcc[i+k][j+k]) >= k:
						ans = max(ans, k+1)
		return ans**2


print(Solution().largest1BorderedSquare(grid = [[1,1,0,0]]))