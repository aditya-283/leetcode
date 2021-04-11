from typing import List
from collections import deque

class Solution:
	def shortestBridge(self, A: List[List[int]]) -> int:
		def nbrs(i, j):
			return [(x, y) for x, y in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= x < len(A)
																			   and 0 <= y < len(A[0])]

		def bfs(s_i, s_j):
			q = deque()
			discovered.add((s_i, s_j))
			q.appendleft((s_i, s_j))
			while q:
				i, j = q.pop()
				A[i][j] = 's'
				for x, y in nbrs(i, j):
					if A[x][y] == 1 and (x, y) not in discovered:
						q.appendleft((x, y))
						discovered.add((x, y))

		def dist(i, j):
			return 0 if A[i][j] == 's' else A[i][j]


		def expand(border):
			while border:
				i, j = border.pop()
				for x, y in nbrs(i, j):
					if A[x][y] == 't':
						return A[i][j]
					if (x, y) not in discovered:
						discovered.add((x, y))
						border.appendleft((x, y))
						A[x][y] = dist(i, j) + 1

		m, n = len(A), len(A[0])
		discovered = set()
		markedFirst = False
		for i in range(m):
			for j in range(n):
				if A[i][j] == 1 and not markedFirst:
					bfs(i, j)
					markedFirst = True
				elif A[i][j] == 1:
					A[i][j] = 't'

		return expand(deque(discovered))


print(Solution().shortestBridge([[1,1,0,0,0],
								 [1,0,0,0,0],
								 [1,0,0,0,0],
								 [0,0,0,1,1],
								 [0,0,0,1,1]]))

