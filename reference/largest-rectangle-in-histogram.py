from typing import List
class Solution:
	def largestRectangleArea(self, histogram):
		stack = list()
		max_area, index = 0, 0
		while index < len(histogram):
			if (not stack) or (histogram[stack[-1]] <= histogram[index]):
				stack.append(index)
				index += 1
			else:
				area = (histogram[stack.pop()] * ((index - stack[-1] - 1) if stack else index))
				max_area = max(max_area, area)
		while stack:
			area = (histogram[stack.pop()] * ((index - stack[-1] - 1) if stack else index))
			max_area = max(max_area, area)
		return max_area
  
print(Solution().largestRectangleArea([2,1,5,6,2,3]))