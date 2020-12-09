from typing import List
from functools import cache

class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int:
		@cache
		def coinChangeHelper(amount):
			if amount == 0:
				return 0
			if amount in coins:
				return 1
			if amount < min(coins):
				return -1
			else:
				arr =  [coinChangeHelper(amount - coin) for coin in coins]
				if any(x > -1 for x in arr):
					return 1 + min([x for x in arr if x > -1])
				else:
					return -1
		return coinChangeHelper(amount)

sol = Solution()
print(sol.coinChange(coins=[1, 9, 19], amount=100))


 1  2  3  4      13  9 5 1
 5  6  7  8  =>  14 10 6 2
 9 10 11 12      15 11 7 3
13 14 15 16      16 12 8 4