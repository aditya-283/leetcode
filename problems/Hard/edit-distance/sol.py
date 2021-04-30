from typing import List
from functools import cache

class Solution:
	def minDistance(self, word1: str, word2: str) -> int:
		@cache
		def editDistance(i, j):
			if i == 0: return j
			elif j == 0: return i
			
			if word1[i-1] == word2[j-1]:
				return editDistance(i-1, j-1)
			return 1 + min(editDistance(i-1, j), editDistance(i, j-1), editDistance(i-1, j-1))
		return editDistance(len(word1), len(word2))



print(Solution().minDistance('aab', 'baab'))