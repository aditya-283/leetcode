from typing import List
# from functools import cache

class Solution:
	# def longestCommonSubsequence(self, text1: str, text2: str) -> int:
	# 	# @cache
	# 	dp = {}
	# 	def longestSubsequenceRec(i, j):
	# 		if (i, j) in dp:
	# 			return dp[i, j]
	# 		if i >= len(text1) or j >= len(text2):
	# 			return 0
	# 		if text1[i] == text2[j]:
	# 			dp[i, j] = 1 + longestSubsequenceRec(i+1, j+1)
	# 		else:
	# 			dp[i, j] = max(longestSubsequenceRec(i, j+1), longestSubsequenceRec(i+1, j))
	# 		return dp[i, j]

	# 	return longestSubsequenceRec(0, 0)



	def longestCommonSubsequence(self, text1, text2):
		n, m = len(text1), len(text2)
		dp = [0]*(n+1)
		for i in range(m-1, -1, -1):
			new_dp = [0] * (n+1)
			for j in range(n-1, -1, -1):
				if text2[i] == text1[j]:
					new_dp[j] = 1 + dp[j+1] 
				else:
					new_dp[j] = max(new_dp[j+1], dp[j])
			dp = new_dp 

		return dp[0]




print(Solution().longestCommonSubsequence("abcde", "ace"))