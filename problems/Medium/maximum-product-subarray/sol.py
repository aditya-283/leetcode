from typing import List
from itertools import accumulate
import operator


def splitAt(arr, x):
	lists = []
	cur = []
	for elem in arr:
		if elem != x:
			cur.append(elem)
		else:
			lists.append(cur)
			cur = []
	lists.append(cur)
	return lists


def range_prod(arr, start, end):
	if start < 0 or end < 0 or start >= len(arr) or end >= len(arr) or start > end:
		return -1*float('inf')
	prods = list(accumulate(arr, operator.mul))
	if start > 0:
		return prods[end]/prods[start-1]
	else:
		return prods[end]


class Solution:
	def maxNonZeroProduct(self, arr):
		neg_indices = [i for i, x in enumerate(arr) if x < 0]
		if len(neg_indices) % 2:
			return max(range_prod(arr, 0, neg_indices[-1]-1), range_prod(arr, neg_indices[0]+1, len(arr)-1))
		else:
			return range_prod(arr, 0, len(arr)-1)

	def maxProduct(self, nums: List[int]) -> int:
		arrs = splitAt(nums, 0)
		ans = -1*float('inf')
		for arr in arrs:
			ans = max(ans, self.maxNonZeroProduct(arr))
		return int(max(ans, max(nums)))


print(Solution().maxProduct([-2, 0, -1]))