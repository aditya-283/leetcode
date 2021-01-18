from typing import List

class Solution:

	def rotatedSearch(self, arr, start, end):
		if start >= end:
			return arr[start]
		
		mid = (start + end) // 2
		if arr[mid] >= arr[0]:
			return self.rotatedSearch(arr, mid+1, end)
		elif arr[mid] < arr[0] and arr[mid] > arr[mid-1]:
			return self.rotatedSearch(arr, start, mid-1)
		elif arr[mid] < arr[0] and arr[mid] < arr[mid-1]:
			return arr[mid]

	def findMin(self, nums: List[int]) -> int:
		return min(nums[0], self.rotatedSearch(nums, 0, len(nums)-1))


print(Solution().findMin([11,13,15,17]))