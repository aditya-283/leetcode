from typing import List
from functools import cache
from itertools import product

class Solution:
	def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
		R, C = len(matrix), len(matrix[0])

		def nbrs(i, j):
			return [(r, c) for r, c in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)) if 0 <= r < R and 0 <= c < C and matrix[r][c] > matrix[i][j]]
		
		@cache
		def longestPathFrom(i, j):
			return 1 + max(longestPathFrom(r, c) for r, c in nbrs(i, j)) if nbrs(i, j) else 1
		return max(longestPathFrom(i, j) for (i, j) in product(range(R), range(C)))


print(Solution().longestIncreasingPath([[1]]))