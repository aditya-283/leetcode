from typing import List

class Solution:
	# sometimes functional in python is uglier
	# def isPalindrome(self, s: str) -> bool:
	# 	alphanum = list(filter(lambda c: ord(c) in range(ord('a'), ord('z')+1) or
	# 					   ord(c) in range(ord('A'), ord('Z')+1) or
	# 					   ord(c) in range(ord('0'), ord('9')+1), list(s)))
	# 	# print(alphanum)
	# 	return ''.join(reversed(alphanum)).lower() == ''.join(alphanum).lower()


	def isPalindrome(self, s):
		filtered_s = [c.lower() for c in s if c.isalnum()]
		return ''.join(filtered_s) == ''.join(reversed(filtered_s))



print(Solution().isPalindrome("A man, a plan, a canal: Panama"))