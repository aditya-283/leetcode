from typing import List

class Solution:
	def canConvert(self, str1: str, str2: str) -> bool:
		map = {}
		for c, d in zip(str1, str2):
			if c not in map:
				map[c] = d
			elif map[c] != d:
				return False
		return True


print(Solution().canConvert(str1 = "leetcode", str2 = "codeleet"))