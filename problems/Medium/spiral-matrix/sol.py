from typing import List


class Solution:
	def spiralOrderRec(self, matrix):
		if not matrix:
			return []
		return list(matrix[0]) + self.spiralOrderRec(list(reversed(list(zip(*matrix[1:])))))

matrix = [[1, 2, 3],
		  [4, 5, 6], 
		  [7, 8, 9],
		  [10, 11, 12]]
print(Solution().spiralOrderRec(matrix))



