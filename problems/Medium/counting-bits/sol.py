from typing import List


class Solution:
	def countBits(self, num: int) -> List[int]:
		result = [0]
		for i in range(1, num+1):
			result.append(result[i//2] + i%2)
		return result
		
print(Solution().countBits(5))