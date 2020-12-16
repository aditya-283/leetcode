from typing import List
from collections import defaultdict, deque, Counter
import sys

class Solution:
	def minWindow(self, s, t):
		s_counter = Counter()
		t_counter = Counter(t)
		chars = len(t_counter.keys())
		answer = ""
		matches = 0
		if len(s) < len(t):
			return ""
		i, j = 0, -1
		while i < len(s):
			if matches < chars: #expand
				j += 1
				if j == len(s):
					return answer
				if s[j] in t_counter.keys():
					s_counter[s[j]] += 1
					if s_counter[s[j]] == t_counter[s[j]]:
						matches += 1
			elif matches == chars: # contract
				if s[i] in t_counter.keys():
					s_counter[s[i]] -= 1
				if s_counter[s[i]] == t_counter[s[i]] - 1:
					matches -= 1
				i += 1

			if matches == chars:
				if not answer or (j - i + 1) < len(answer):
					answer = s[i:j+1]
		return answer


print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "aa"))