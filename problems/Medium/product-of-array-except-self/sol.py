from typing import List
from itertools import accumulate
import operator


class Solution:
	def productExceptSelf(self, nums: List[int]) -> List[int]:
		productsLeft = list(accumulate(nums, operator.mul))
		productsRight = list(reversed(list(accumulate(reversed(nums), operator.mul))))
		res = []
		for i, num in enumerate(nums):
			if i == 0:
				res.append(productsRight[1])
			elif i == len(nums)-1:
				res.append(productsLeft[-2])
			else:
				res.append(productsLeft[i-1]*productsRight[i+1])

		return res

print(Solution().productExceptSelf([1, 2, 3, 4]))
