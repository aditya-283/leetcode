from typing import List
from functools import cache
from bisect import bisect_left

class Solution:
	def wordsTyping(self, sentence: List[str], rows: int, cols: int) -> int:
		def wordsFit(i):
			spaceTaken = sentence[i]
			count = 0
			while spaceTaken < cols:
				i = (i + 1) % len(sentence)
				count += 1
				spaceTaken += len(sentence[i]) + 1
			return count

		wv = {}
		for i in range(len(sentence)):
			wc[i] = wordsFit(i)

		words, i = 0, 0
		for r in range(rows):
			words += wc[i]
			i += wc[i]
		return words // len(sentence)





print(Solution().wordsTyping(["f","p","a"], 8, 7))