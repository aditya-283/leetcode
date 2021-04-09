from typing import List


class Solution:
	def isAlienSorted(self, words: List[str], order: str) -> bool:
		order_ = {c:i for i, c in enumerate(order)}
		for w1, w2 in zip(words, words[1:]):
			for c1, c2 in zip(w1, w2):
				if c1 != c2:
					if order_[c1] > order_[c2]:
						return False
					break
			else:
				if len(w1) > len(w2):
					return False
		return True


print(Solution().isAlienSorted(["word","world","row"], "worldabcefghijkmnpqstuvxyz"))