from typing import List
from collections import deque
from itertools import product
from math import inf
class Solution:
	def removeInvalidParentheses(self, s: str) -> List[str]:
		def nbrs(s):
			return set(s[:i] + s[i+1:] for i in range(len(s)) if s[i] in ('(', ')'))

		def isValid(s):
			a = deque()
			for c in s:
				if c == '(':
					a.append(c)
				elif c == ')':
					if a:
						a.pop()
					else:
						return False
			return not a

		maxDepth = inf
		q, visited = deque([(s, 0)]), set([s])
		ans = []
		while q:
			cur, depth = q.pop()
			if isValid(cur):
				maxDepth = min(maxDepth, len(s) - len(cur))
				ans.append(cur)
				continue
			if depth < maxDepth or depth == 0:
				for nbr in nbrs(cur):
					if nbr not in visited:
						visited.add(nbr)
						q.appendleft((nbr, depth + 1))
		return ans


# print(Solution().removeInvalidParentheses("(())"))

print(Solution().removeInvalidParentheses("(a)())()"))
