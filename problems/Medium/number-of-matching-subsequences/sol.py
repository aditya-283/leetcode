from typing import List
from collections import deque

class Solution:
	def numMatchingSubseq(self, s: str, words: List[str]) -> int:
		qwords = [deque(word) for word in words]
		cnt = 0
		for c in s:
			for i in range(len(qwords)):
				if qwords[i] and c == qwords[i][0]:
					qwords[i].popleft()

		return len([i for i in range(len(words)) if not qwords[i]])



print(Solution().numMatchingSubseq(s = "abcde", words = ["a","bb","acd","ace"]))