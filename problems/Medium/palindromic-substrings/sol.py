from typing import List
import itertools

class Solution:
	def countSubstrings(self, s: str) -> int:
		l = len(s)
		dp = [[0]*l for _ in range(l)]
		for j in range(len(s)):
			for i in range(j, -1, -1):
				if i == j:
					dp[i][j] = True
				elif s[i] == s[j] and i == j - 1:
					dp[i][j] = True
				elif s[i] == s[j] and i < j - 1:
					dp[i][j] = dp[i+1][j-1]
				else:
					dp[i][j] = False

		# count = 0
		# for i in range(l):
		# 	for j in range(i, l):
		# 		if dp[i][j] == True:
		# 			count += 1
		# return count
		return list(itertools.chain(*dp)).count(True)


print(Solution().countSubstrings("abc"))