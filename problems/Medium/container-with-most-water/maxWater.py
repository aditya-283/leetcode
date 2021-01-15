from collections import deque
from itertools import accumulate
from typing import List
import bisect


def bisectLeft(self, arr):


def bisectRight(self, arr):
	



class Solution:
	def maxWater(self, height: List[int]) -> int:
		cum_max_left = list(accumulate(height, max))
		cum_max_right = list(accumulate(reversed(height), max))
		maxWater = 0
		n = len(height)
		for i, h in enumerate(height):
			firstGTELeft = bisect.bisect_left(cum_max_left, h, hi=i)
			firstGTERight = n-1-bisect.bisect_left(cum_max_right, h, hi=n-i-1)
			maxWater = max(maxWater, h*(i-firstGTELeft), h*(firstGTERight-i))
		return maxWater
		
if __name__ == '__main__':
	sol = Solution()
	a = [1,8,6,2,5,4,8,3,7]
	print('Ans: ', sol.maxWater(a))
