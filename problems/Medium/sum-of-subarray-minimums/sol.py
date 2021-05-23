from typing import List
from collections import deque

class Solution:
	def sumSubarrayMins(self, arr: List[int]) -> int:
		n = len(arr)
		def calculateLeftMinLimits(): #exclusive limits - for minimum, we calculate nearest element less
			stack = deque()
			idx = 0
			nearestLeftGreater = [-1]*n
			while idx < n:
				if stack and arr[stack[-1]] >= arr[idx]:
					stack.pop()
				else:
					nearestLeftGreater[idx] = stack[-1] if stack else -1
					stack.append(idx)
					idx += 1
			return nearestLeftGreater

		def calculateRightMinLimits(): #exclusive limits - for minimum, we calculate nearest element less
			stack = deque()
			idx = n-1
			nearestRightGreater = [-1]*n
			while idx >= 0:
				if stack and arr[stack[-1]] > arr[idx]:
					stack.pop()
				else:
					nearestRightGreater[idx] = stack[-1] if stack else -1
					stack.append(idx)
					idx -= 1
			return nearestRightGreater

		nearestLeftGreater = calculateLeftMinLimits()
		nearestRightGreater = calculateRightMinLimits()
		ans = 0
		for i in range(n):
			leftLimit = nearestLeftGreater[i] + 1 if nearestLeftGreater[i] != - 1 else 0
			rightLimit = nearestRightGreater[i] - 1 if nearestRightGreater[i] != -1 else n-1
			ans += (rightLimit - i + 1)*(i - leftLimit + 1)*arr[i]
		return ans % 1000000007

print(Solution().sumSubarrayMins([71,55,55]))

