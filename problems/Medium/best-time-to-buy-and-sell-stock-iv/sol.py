from typing import List
from functools import cache


class Solution:
	def maxProfit(self, k: int, prices: List[int]) -> int:
		@cache
		def profitHelper(k, pos, buy):
			if not prices or not k or pos >= len(prices):
				return 0

			if buy:
				return max(profitHelper(k, pos+1, 0) - prices[pos], profitHelper(k, pos+1, 1))
			else:
				return max(profitHelper(k-1, pos+1, 1) + prices[pos], profitHelper(k, pos+1, 0))

		return profitHelper(k, 0, 1)




print(Solution().maxProfit(2, [1, 3, 5, 2, 5, 1, 6]))