from typing import List

class Solution:
	def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
		def intersection(a, b):
			if b[1] >= a[1] >= b[0] or \
			   b[1] >= a[0] >= b[0] or \
			   a[0] <= b[0] <= a[1] or \
			   a[1] <= b[1] <= a[1]:
					return [max(a[0], b[0]), min(a[1], b[1])]
			else:
				return []

		i, j = 0, 0
		res = []
		while i < len(firstList) and j < len(secondList): #reconsider
			int_i_j = intersection(firstList[i], secondList[j])
			if int_i_j:
				res.append(int_i_j)
			if firstList[i][1] > secondList[j][1]:
				j += 1
			elif firstList[i][1] < secondList[j][1]:
				i += 1
			else:
				i += 1
				j += 1

		return res

print(Solution().intervalIntersection([[1,3],[5,9]], [[2, 3], [6, 7]]))