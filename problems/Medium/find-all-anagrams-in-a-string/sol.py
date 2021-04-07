from typing import List
from collections import Counter

class Solution:
	def findAnagrams(self, s: str, p: str) -> List[int]:
		i, j, n, ans = 0, len(p), len(s), []
		s_counter, p_counter = Counter(s[i:j]), Counter(p)
		while i <= len(s) - len(p):
			if s_counter == p_counter:
				ans.append(i)
			s_counter[s[i]] -= 1
			if s_counter[s[i]] == 0:
				del s_counter[s[i]]
			i += 1
			if j < len(s):
				s_counter[s[j]] += 1
				j += 1
		return ans

print(Solution().findAnagrams("cbaebabacd", "abc"))