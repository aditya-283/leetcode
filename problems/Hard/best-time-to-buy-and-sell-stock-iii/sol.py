from typing import List
from itertools import accumulate

class Solution:
	# OK O(n^2) algorithm, can be made O(n)
	def maxProfit(self, prices: List[int]) -> int:
		n = len(prices)
		min_until = list(accumulate(prices, min))
		max_from = list(reversed(list(accumulate(reversed(prices), max))))
		profits_till_i = list(accumulate([prices[i] - min_until[i] for i in range(n)], max))
		profits_from_i = list(reversed(list(accumulate(reversed([max_from[i] - prices[i] for i in range(n)]), max))))
		return max(profits_till_i[i] + profits_from_i[i] for i in range(n))

print(Solution().maxProfit([1,2,3,4,5]))