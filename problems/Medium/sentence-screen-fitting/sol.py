from typing import List
from functools import cache
from bisect import bisect_left

class Solution:
	def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
		i, n = 0, len(sentence)
		r, c = rows, cols
		lengths = [len(word) for word in sentence]

		if max(lengths) > cols:
			return 0

		ans = 0
		dp = {}
		nxt = {}
		for r in range(rows):
			if i not in dp:
				dp[i] = 0
				stops = [sum(x) for x in zip(lengths, range(n))]
				while bisect_left(stops, cols) == n:
					cols -= 
				print(i_)
				if i_ == n:

				nxt[i] = bisect_left(stops, cols)
				ans += dp[i]
			else:
				ans += dp[i]
				i = nxt[i]
		return ans






print(Solution().wordsTyping(["f","p","a"], 8, 7))