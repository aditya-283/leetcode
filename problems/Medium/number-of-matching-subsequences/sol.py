from typing import List

class Solution:
	def numMatchingSubseq(self, s: str, words: List[str]) -> int:
		def isSubstring(a, b):
			i = 0
			for c in b:
				if a[i] == c:
					i += 1
					if i == len(a):
						return True
			return False

		cnt = 0
		seenTrue = set()
		seenFalse = set()
		for word in words:
			if word in seenTrue:
				cnt += 1
			elif word in seenFalse:
				continue
			elif isSubstring(word, s):
				seenTrue.add(word)
				cnt += 1
			else:
				seenFalse.add(word)
		return cnt


print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))