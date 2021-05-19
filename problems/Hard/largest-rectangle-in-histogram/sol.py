from typing import List

class Solution:
	def largestRectangleArea(self, heights: List[int]) -> int:
		stack = [-1]
		max_area = 0
		for i in range(len(heights)):
			while stack[-1] != -1 and heights[stack[-1]] >= heights[i]:
				print(i, [heights[j] for j in stack])
				current_height = heights[stack.pop()]
				current_width = i - stack[-1] - 1
				print(i, [heights[j] for j in stack])
				print(heights[i], '->', current_width, current_height)
				max_area = max(max_area, current_height * current_width)
			stack.append(i)

		print([heights[i] for i in stack[1:]])
		while stack[-1] != -1:
			current_height = heights[stack.pop()]
			current_width = len(heights) - stack[-1] - 1

			max_area = max(max_area, current_height * current_width)
		return max_area
 
print(Solution().largestRectangleArea([2,1,5,6,2,3]))from typing import List
