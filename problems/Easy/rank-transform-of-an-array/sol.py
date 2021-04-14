from typing import List

class Solution:
	def arrayRankTransform(self, arr: List[int]) -> List[int]:
		inOrder = sorted(arr)
		ranks = {}
		count = 0
		prev = float('-inf')
		for num in inOrder:
			if num > prev:
				count += 1
				prev = num
			ranks[num] = count
			
		return [ranks[i] for i in arr]
