from typing import List
from functools import cache

class Solution:
	@cache
	def uniquePathsFrom(self, m, n, row, col):
		if row == m - 1 and col == n - 1:
			return 1
		elif row == m - 1:
			return self.uniquePathsFrom(m, n, row, col+1)
		elif col == n - 1:
			return self.uniquePathsFrom(m, n, row+1, col)
		else:
			return self.uniquePathsFrom(m, n, row+1, col) + self.uniquePathsFrom(m, n, row, col+1)


	def uniquePaths(self, m: int, n: int) -> int:
		return self.uniquePathsFrom(m, n, 0, 0)


print(Solution().uniquePaths(3, 7))