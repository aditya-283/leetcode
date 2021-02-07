from typing import List

class Solution:
	def maxProfit(self, prices: List[int]) -> int:
		return sum([nxt-cur for cur, nxt in zip(prices, prices[1:]) if nxt > cur])


print(Solution().maxProfit([7,1,5,3,6,4]))