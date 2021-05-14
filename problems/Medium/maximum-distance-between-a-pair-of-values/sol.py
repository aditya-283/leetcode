from typing import List
from bisect import bisect_left
class Solution:
	def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
		revNums2 = list(reversed(nums2))
		m, n = len(nums1), len(nums2)
		ans = 0
		for i, num in enumerate(nums1):
			idx = bisect_left(revNums2, num, 0, n-1-i)
			j = n - 1 - idx
			ans = max(ans, j - i)
			print(i, j)
		return ans


print(Solution().maxDistance(nums1 = [5,4], nums2 = [3,2]))