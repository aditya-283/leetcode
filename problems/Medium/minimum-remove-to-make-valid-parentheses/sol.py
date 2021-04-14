from typing import List

# class Solution:
# 	def minRemoveToMakeValid(self, s: str) -> str:
# 		parens = []
# 		remove = []
# 		for i, c in enumerate(s):
# 			if c == '(':
# 				parens.append(i)
# 			elif c == ')':
# 				if not parens:
# 					remove.append(i)
# 				else:
# 					parens.pop()
# 		remove.extend(parens)
# 		return ''.join([c for i, c in enumerate(s) if i not in remove])


# print(Solution().minRemoveToMakeValid("a)b(c)d"))


