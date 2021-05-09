from typing import List
from itertools import cycle

class Solution:
	def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
		def isValid(r, c):
			return 0 <= r < R and 0 <= c < C
		
		def corners(R, C):
			return [(0, 0), (0, C-1), (R-1, C-1), (R-1, 0)]
				
		cycle = [(0, 1), (1, 0), (0, -1), (-1, 0)]
		spiral = set()
		leg_length = 0
		r, c = r0, c0
		while True:
			if all((r, c) in spiral for r, c in corners(R, C)):
				break
			
			rot = 0
			for r_inc, c_inc in cycle:
				spiral.add((r, c))
				if not rot%2:
					leg_length += 1
				for l in range(leg_length):
					r += r_inc
					c += c_inc
				rot += 1
				
			
		return list(spiral)from typing import List
