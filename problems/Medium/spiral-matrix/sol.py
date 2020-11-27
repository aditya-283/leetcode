from typing import List


class Solution:
	def spiralOrderRec(self, matrix):
		if len(matrix) == 0:
			return []
		return matrix[0] + self.spiralOrder(list(reversed([list(v) for v in list(zip(*matrix[1:]))])))
	
	def spiralOrder(self, matrix):
		l = []
		while len(matrix) > 0:
			l += matrix.pop(0)
			matrix = list(reversed([list(v) for v in list(zip(*matrix))]))
		return l

matrix = [[1, 2, 3],
		  [4, 5, 6], 
		  [7, 8, 9],
		  [10, 11, 12]]
print(Solution().spiralOrderRec(matrix))



