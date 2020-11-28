from typing import List
from collections import defaultdict
from functools import cache
from timeit import repeat


def appendNums(lists, num, i):
		return [list + [num]*i for list in lists]

class Solution:
	def combinationSumRec(self, candidates, target, till, dp):		
		if (target, till) in dp:
			return dp[(target, till)]
		if not target:
			return [[]]
		if till == -1 or not candidates:
			return []
		else:
			sums = []
			for i in range(int(target/candidates[till]) + 1):
				till_last = self.combinationSumRec(candidates, target-i*candidates[till], till-1, dp)
				sums.extend(appendNums(till_last, candidates[till], i))
			dp[(target, till)] = sums
		return dp[(target, till)]

	def combinationSumPure(self, candidates, target):
		if not target:
			return [[]]
		if not candidates:
			return []
		else:
			sums = []
			for i in range(int(target/candidates[-1]) + 1):
				till_last = self.combinationSumPure(candidates[:-1], target-i*candidates[-1])
				sums.extend(appendNums(till_last, candidates[-1], i))
			return sums


	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		dp = defaultdict(lambda : -1)
		# return self.combinationSumPure(sorted(candidates), target)
		return self.combinationSumRec(sorted(candidates), target, len(candidates)-1, dp)

sol = Solution()
print(sol.combinationSum([2, 3, 5], 8))
# setup_code = "from __main__ import Solution"
# stmt = "Solution().combinationSum([2, 3, 5], 400)"
# times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)
# print(f"Minimum execution time: {min(times)}")