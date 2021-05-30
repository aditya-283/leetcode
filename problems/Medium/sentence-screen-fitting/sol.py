from typing import List
from functools import cache
from bisect import bisect_left

class Solution:
	def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
		def wordsFit(i):
			c = cols
			count = 0
			while len(sentence[i]) <= c:
				c -= len(sentence[i]) + int(len(sentence[i]) < c)
				i = (i + 1) % len(sentence)
				count += 1
			return count

		wc = {}
		for i in range(len(sentence)):
			wc[i] = wordsFit(i)

		words, i = 0, 0
		for r in range(rows):
			words += wc[i]
			i = (i + wc[i]) % len(sentence)
		return words // len(sentence)

print(Solution().wordsTyping(["f","p","a"], 8, 7))