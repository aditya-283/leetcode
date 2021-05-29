
from typing import List
from functools import cache
from itertools import product

class Solution:
	def longestLine(self, matrix: List[List[int]]) -> int:
		directions = {'bottom': (1, 0), 'right': (0, 1), 'bottom-left': (1, -1), 'bottom-right': (1, 1)}
		R, C = len(matrix), len(matrix[0])

		@cache
		def longestLineRec(i, j, d):
			r, c = i + directions[d][0], j + directions[d][1]
			if matrix[i][j] == 1 and 0 <= r < R and 0 <= c < C:
				return 1 + longestLineRec(r, c, d) 
			else:
				return matrix[i][j]
		return max(longestLineRec(r, c, d) for r, c in product(range(R), range(C)) for d in directions)

print(Solution().longestLine([[1,1,1,1],[0,1,1,0],[0,0,0,1]]))