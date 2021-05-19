from typing import List
from functools import cache
from collections import deque
class Solution:
	def maximalRectangle(self, matrix: List[List[str]]) -> int:
		if not matrix or not matrix[0]:
			return 0
		R, C = len(matrix), len(matrix[0])
		maxConsecInRow = [[0]*C for _ in range(R)]
		for i in range(R):
			for j in range(C):
				if matrix[i][j] == '1':
					maxConsecInRow[i][j] = maxConsecInRow[i][j-1] + 1 if j > 0 else 1

		maximalRectangleEndingAt = [[0]*C for _ in range(R)]
		maxArea = 0
		for j in range(C):
			widths = [maxConsecInRow[i][j] for i in range(R)]
			maxArea = max(maxArea, self.largestRectangleArea(widths))
		return maxArea

	def largestRectangleArea(self, heights):
		stack = deque()
		index, maxArea = 0, 0
		while index < len(heights):
			if not stack or heights[index] >= heights[stack[-1]]:
				stack.append(index)
				index += 1
			else:
				height = heights[stack.pop()]
				width = (index - 1 - stack[-1]) if stack else index
				area = height * width
				maxArea = max(area, maxArea)
		while stack:
				height = heights[stack.pop()]
				width = (index - 1 - stack[-1]) if stack else index
				area = height * width
				maxArea = max(area, maxArea)
		return maxArea

print(Solution().maximalRectangle(matrix = [["0","0","0","0","0","0","1"],
											["0","0","0","0","1","1","1"],
											["1","1","1","1","1","1","1"],
											["0","0","0","1","1","1","1"]]))