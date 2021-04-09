from typing import List

class Solution:
	def customSortString(self, S: str, T: str) -> str:
		order_ = {c: i for i, c in enumerate(S)}
		return ''.join(sorted(T, key=lambda x: order_[x] if x in order_ else 99))

print(Solution().customSortString("cba", "abcd"))