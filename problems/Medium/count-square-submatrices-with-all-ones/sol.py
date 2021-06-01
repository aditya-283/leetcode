from typing import List
from functools import cache

class Solution:
	def countSquares(self, matrix: List[List[int]]) -> int:

		def totalSquares(k):
			return sum((i+1)**2 for i in range(k))

		R, C = len(matrix), len(matrix[0])
		@cache
		def maxSquareSize(i, j):
			if i < 0 or j < 0:
				return 0
			if matrix[i][j] == 0:
				return 0
			if matrix[i][j] == 1:
				left = maxSquareSize(i, j-1) if matrix[i][j-1] else 0
				top = maxSquareSize(i-1, j) if matrix[i-1][j] else 0
				k = min(left, top)
				return k + int(matrix[i-k][j-k] == 1)

		squareSize = [[0]* C for _ in range(R)]
		for i in range(R):
			for j in range(C):
				squareSize[i][j] = maxSquareSize(i, j)

		return sum(sum(row) for row in squareSize)


print(Solution().countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]))