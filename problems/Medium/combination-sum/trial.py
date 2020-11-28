from typing import List
from functools import cache


def appendNums(lists, num, i):
		return [list + [num]*i for list in lists]

class Solution:
	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		@cache
		def combinationSumRec(target, till):		
			if not target:
				return [[]]
			if till == -1 or not candidates:
				return []
			else:
				sums = []
				for i in range(int(target/candidates[till]) + 1):
					till_last = combinationSumRec(target-i*candidates[till], till-1)
					sums.extend(appendNums(till_last, candidates[till], i))
				return sums

		return combinationSumRec(target, len(candidates)-1)

# sol = Solution([2, 3, 5])
# print(sol.combinationSum([2, 3, 5], 18))
from timeit import repeat

setup_code = "from __main__ import Solution"
stmt = "Solution().combinationSum([2, 3, 5], 400)"
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
print(f"Minimum execution time: {min(times)}")
