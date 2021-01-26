from typing import List

class Solution:
	def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
		def reachesPacific(i, j):
			if i < 0 or j < 0:
				return True
			return (matrix[i][j] > matrix[i-1][j] and reachesPacific(i-1, j)) or 
					(matrix[i][j] > matrix[i][j-1] and reachesPacific(i, j-1))

		def reachesAtlantic(i, j):
			if i >= R or j >= C:
				return True
			return (matrix[i][j] > matrix[i+1][j] and reachesAtlantic(i+1, j)) or 
					(matrix[i][j] > matrix[i][j+1] and reachesPacific(i, j+1))

		R, C = len(matrix), len(matrix[0])
		result = []
		for i in range(R):
			for j in range(C):
				if reachesPacific(i, j) and reachesAtlantic(i, j):
					result.append([i, j])
		return result








print(Solution([[1, 2, 2, 3, 5],
[3, 2, 3, 4, 4],
[2, 4, 5, 3, 1],
[6, 7, 1, 4, 5],
[5, 1, 1, 2, 4]]).pacificAtlantic())from typing import List
