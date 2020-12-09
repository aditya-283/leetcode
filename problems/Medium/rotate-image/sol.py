from typing import List


class Solution:
	def transpose(self, matrix):
		n = len(matrix)
		for i in range(n):
			for j in range(i):
				matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
		return matrix

	def y_mirror(self, matrix):
		n = len(matrix)
		for i in range(n):
			for j in range(n//2):
				matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
		return matrix

	def rotate(self, matrix: List[List[int]]) -> None:
		return self.y_mirror(self.transpose(matrix))


print(Solution().rotate([[1, 2], [3, 4]]))
