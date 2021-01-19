from typing import List



class Solution:
	def hammingWeight(self, n: int) -> int:
		return list('{0:b}'.format(n)).count('1')


print(Solution().hammingWeight(5))