from collections import defaultdict, Counter

class Solution:
	def numSplits(self, s: str) -> int:
		c, d, ans = defaultdict(int), Counter(s), 0
		for i in range(len(s)-1):
			c[s[i]] += 1
			d[s[i]] -= 1
			if d[s[i]] == 0:
				del d[s[i]]

			if len(c.keys()) == len(d.keys()):
				ans += 1
		return ans


print(Solution().numSplits(s = "aacaba"))