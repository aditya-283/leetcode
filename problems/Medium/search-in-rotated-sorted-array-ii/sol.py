from typing import List

class Solution:
	def search(self, nums: List[int], target: int) -> bool:
		def searchHelper(nums, target, start, end):
			mid = (start + end) // 2 
			# print(nums[start], nums[mid], nums[end])

			if target == nums[start]:
				return True

			if target == nums[mid]:
				return True

			if start >= end:
				return False


			if nums[mid] < nums[start]:
				if target < nums[mid] or target > nums[start]:
					return searchHelper(nums, target, start, mid-1)
				elif target < nums[start]: #for target both < and > nums[start]
					return searchHelper(nums, target, mid+1, end)
			elif nums[mid] == nums[start]:
				return searchHelper(nums, target, start, mid-1) or searchHelper(nums, target, mid+1, end)
			else:
				if target < nums[start] or target > nums[mid]:
					return searchHelper(nums, target, mid+1, end)
				else:
					return searchHelper(nums, target, start, mid-1)
		return searchHelper(nums, target, 0, len(nums)-1) 


