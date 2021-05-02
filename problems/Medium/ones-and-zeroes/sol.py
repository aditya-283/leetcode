from typing import List
from functools import cache

class Solution:
	def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
		@cache
		def findMaxUtil(i, m, n):
			if (m == 0 and n == 0) or (i == len(arr)):
				return 0

			if arr[i][0] <= m and arr[i][1] <= n:
				return max(1 + findMaxUtil(i+1, m-arr[i][0], n-arr[i][1]), findMaxUtil(i+1, m, n))
			else:
				return findMaxUtil(i+1, m, n)
		arr = [(s.count('0'), s.count('1')) for s in strs]
		return findMaxUtil(0, m, n)

print(Solution().findMaxForm(["10","0001","111001","1","0"], m = 5, n = 3))

