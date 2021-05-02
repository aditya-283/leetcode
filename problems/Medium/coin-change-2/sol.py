from typing import List
from functools import cache

class Solution:
	def change(self, amount: int, coins: List[int]) -> int:
		@cache
		def changeCountUtil(i, amt):
			if amt == 0: return 1
			elif amt < 0 or i == len(coins): return 0
			return sum(changeCountUtil(i+1, amt - j*coins[i]) for j in range(amt // coins[i] + 1))
		coins.sort(reverse=True)
		return changeCountUtil(0, amount)

print(Solution().change(5, [1, 2, 5]))
# 5 [1, 2, 5]

# CCU 0 5
# 	choices = 5
# 	1+ 1 + 1 + 1 + 0 + 1


# CCU 1 1
# 	choices = 0
# 	CCU 2 1
# 	= 0

# CCU 2 1
# 	choices = 0
# 	CCU 3 1
# 	= 0

# CCU 1 2
# 	choices = 1
# 	= 1

# CCU 1 5
# 	choices = 2
# 	= 1

# CCU 1 4
# 	choices = 2
# 	CCU 2 4 CCU 2 2 CCU 2 0