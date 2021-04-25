from typing import List
from collections import deque

class Solution:
	def simplifyPath(self, path: str) -> str:
		items = path.split('/')
		stack = deque()
		for item in items:
			if not item:
				continue

			if item == '..':
				if stack:
					stack.pop()
			elif item != '.':
				stack.append(item)
		return '/' + '/'.join(item for item in stack)

print(Solution().simplifyPath("/a/./b/../../c/"))