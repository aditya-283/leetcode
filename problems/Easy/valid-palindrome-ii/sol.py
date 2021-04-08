from typing import List
from functools import cache

class Solution:
	def validPalindrome(self, s: str) -> bool:
		# @cache
		# def validPalindromeRec(i, j, mistakeCommitted):
		# 	if i >= j:
		# 		return True
		# 	if s[i] == s[j]:
		# 		return validPalindromeRec(i+1, j-1, mistakeCommitted)
		# 	elif not mistakeCommitted:
		# 		return validPalindromeRec(i+1, j, True) or validPalindromeRec(i, j-1, True)
		# 	else:
		# 		return False
		# return validPalindromeRec(0, len(s)-1, False)
		i, j = 0, len(s) - 1
		mistakeCommitted = False
		while True:
			if i >= j:
				return True
			if s[i] == s[j]:
				i += 1
				j -= 1
			elif mistakeCommitted:
				return False
			else:
				delete_i = s[:i] + s[i+1:]
				delete_j = s[:j] + s[j+1:]
				return delete_i == delete_i[::-1] or delete_j == delete_j[::-1]



print(Solution().validPalindrome('attbcbta'))