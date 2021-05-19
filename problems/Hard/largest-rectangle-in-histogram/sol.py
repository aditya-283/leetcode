from typing import List
from collections import deque
class Solution:
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
  
# print(Solution().largestRectangleArea([2,1,5,6,2,3]))



# 4 functions into 1
def adjacentElem(arr, fromStart=True, lessThan=True):
	def compare(x, y):
		return arr[stack[-1]] > arr[index] if lessThan else arr[stack[-1]] < arr[index] 

	iterator = iter(range(len(arr))) if fromStart else iter(range(len(arr)-1, -1, -1))
	stack = deque()
	index = next(iterator)
	lastLessThan = [-1]*len(arr)
	try:
		while True:
			if stack and compare(arr[stack[-1]], arr[index]):
				stack.pop()
			else:
				lastLessThan[index] = stack[-1] if stack else -1
				stack.append(index)
				index = next(iterator)
	except StopIteration:
		print("Python's iterator API is not pretty :(")
	finally:
		return lastLessThan


print(adjacentElem([2,1,5,6,2,3], True, False))
from typing import List
