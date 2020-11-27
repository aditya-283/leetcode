from operator import add
from functools import reduce

class Solution:
	def twoDimIndices(self, m, n):
		return [[(i, j) for j in range(n)] for i in range(m)]

	def spiralOrderIndices(self, indices):
		if not indices:
			return []
		return list(indices[0]) + self.spiralOrderIndices(list(reversed(list(zip(*indices[1:])))))

	def fill(self, matrix, indices, values):
		for index, value in zip(indices, values):
			matrix[index[0]][index[1]] = value
		return matrix

	def generateMatrix(self, n):
		empty = [[0] * n for i in range(n)]
		return self.fill(empty, self.spiralOrderIndices(self.twoDimIndices(n, n)), range(1, 1 + n**2))

if __name__ == '__main__':
	n = 3
	sol = Solution()
	print()
