from typing import List
from functools import cache

class Solution:
	def maximalSquare(self, matrix: List[List[str]]) -> int:
		@cache
		def maximalSquareEndingAt(i, j):
			if  matrix[i][j] == '1' and (i == 0 or j == 0):
				return 1
			elif matrix[i][j] == matrix[i-1][j] == matrix[i][j-1] == '1':
				common = min(maximalSquareEndingAt(i-1, j), maximalSquareEndingAt(i, j-1))
				if matrix[i-common][j-common] == '1':
					return common + 1
				else:
					return common
			elif matrix[i][j] == '1':
				return 1
			else:
				return 0
		return max(maximalSquareEndingAt(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))**2

print(Solution().maximalSquare(matrix = [["0"]]))from typing import List
