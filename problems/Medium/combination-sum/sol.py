from typing import List
from collections import defaultdict

def appendNums(lists, num, i):
		return [list + [num]*i for list in lists]

def hash(target, idx):
	return f'{target}-{idx}'

class Solution:
	def combinationSumRec(self, candidates, target, till, dp):		
		if hash(target, till) in dp:
			return dp[hash(target, till)]
		if not target:
			return [[]]
		if till == -1 or not candidates:
			return []
		else:
			sums = []
			for i in range(int(target/candidates[till]) + 1):
				till_last = self.combinationSumRec(candidates, target-i*candidates[till], till-1, dp)
				sums.extend(appendNums(till_last, candidates[till], i))
			dp[hash(target, till)] = sums
		return dp[hash(target, till)]

	def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
		dp = defaultdict(lambda : -1)
		return self.combinationSumRec(sorted(candidates), target, len(candidates)-1, dp)

sol = Solution()
print(sol.combinationSum([3,4,5,6], 8))