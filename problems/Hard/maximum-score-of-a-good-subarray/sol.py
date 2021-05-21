from typing import List
from collections import deque

class Solution:
	def maximumScore(self, nums: List[int], k: int) -> int:
		def getFirstLess(arr, left=True):
			firstLess = []
			s = deque()
			if left:
				iterator = enumerate(arr)
			else:
				iterator = reversed(list(enumerate(arr)))

			for i, x in iterator:
				while s and s[-1][0] >= x:
					s.pop()
				if s:
					firstLess.append(s[-1][1])
				else:
					firstLess.append(-1)
				s.append((x,i))
			return firstLess if left else list(reversed(firstLess))

		def largestRectangleArea(height: List[int], k) -> int:
			fll = getFirstLess(height, left=True)
			flr = getFirstLess(height, left=False)
			maxArea = 0
			for i, h in enumerate(height):
				leftLimit = fll[i]+1
				rightLimit = flr[i]-1 if flr[i] > 0 else len(height)-1
				if leftLimit <= k <= rightLimit:
					maxArea = max(maxArea, h*(rightLimit-leftLimit+1))
			return maxArea

		return largestRectangleArea(nums, k)

print(Solution().maximumScore(nums = [5,5,4,5,4,1,1,1], k = 0))

