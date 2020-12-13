from typing import List

class Solution:
	def setZeroes(self, matrix: List[List[int]]) -> None:
		zero_rows, zero_cols = set(), set()
		for i, row in enumerate(matrix):
			for j, x in enumerate(row):
				if x == 0:
					zero_rows.add(i)
					zero_cols.add(j)

		for i, row in enumerate(matrix):
			for j, x in enumerate(row):
				if i in zero_rows or j in zero_cols:
					matrix[i][j] = 0
				else:
					matrix[i][j] = x



print(Solution().setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))