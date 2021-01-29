from typing import List
from collections import defaultdict

class Solution:
	def characterReplacement(self, s: str, k: int) -> int:
		# def maxLengthSubstring(s, c):
		# 	start, end = 0, 0
		# 	count, maxLength = 0, 0
		# 	while start <= end < len(s):
		# 		if s[end] == c:
		# 			count += 1

		# 		if (end-start+1) - count > k:
		# 			if s[start] == c:
		# 				count -= 1
		# 			start += 1
		# 		else:
		# 			maxLength = max(maxLength, end-start+1)

		# 		end += 1
		# 	return maxLength





		vocab = set(s)
		start, end = 0, 0
		maxLength = 0
		counts = defaultdict(int)
		while start <= end < len(s):
			counts[s[end]] += 1
			maxCount = max(counts.values())
			if (end-start+1) - maxCount > k:
				counts[s[start]] -= 1
				start += 1
			else:	
				maxLength = max(maxLength, end-start+1)
			end += 1
		return maxLength


print(Solution().characterReplacement('BAAAB', 2))


