from typing import List
from functools import cache
import operator

# class Solution:
# 	def numRollsToTarget(self, d: int, f: int, target: int) -> int:
# 		def nCrMod(n, r, p):
# 			if n == 0 and r == 0:
# 				return 1
# 			num, denom = 1, 1
# 			for i in range(r):
# 				num   = num * (n - i) % p
# 				denom = denom * (i + 1) % p
# 			return num * pow(denom, p-2, p) % p

# 		i, res = 0, 0
# 		p = pow(10, 9) + 7
# 		while i*f <= (target - d):
# 			res += (pow(-1, i) * (nCrMod(d, i, p) * nCrMod(target - i*f - 1, d - 1, p) % p))
# 			i += 1
# 		return res % p


class Solution:
	def numRollsToTarget(self, d: int, f: int, target: int) -> int:
		dp = [0] * (target+1)
		dp[0] = 1

		for i in range(1, d+1):
			new_dp = [0] * (target+1)
			for t in range(target+1):
				new_dp[t] = sum(dp[t-choice] for choice in range(1, min(t, f) + 1)) % (pow(10, 9) + 7)
			dp = new_dp
		return dp[target]

# class Solution:
# 	@cache
# 	def numRollsToTarget(self, d: int, f: int, target: int) -> int:
# 		if d == 0:
# 			return int(target == 0)
# 		return sum(self.numRollsToTarget(d-1, f, target-choice) for choice in range(1, min(target, f) + 1)) % (pow(10, 9) + 7)

print(Solution().numRollsToTarget(30, 30, 500))