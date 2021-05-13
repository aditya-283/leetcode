from typing import List
from collections import deque

class Solution:
	def slidingPuzzle(self, board: List[List[int]]) -> int:
		s = ''.join(str(x) for x in board[0] + board[1])
		q = deque([(s, s.index('0'), 0)])
		row, col, visited = len(board), len(board[0]), {s}
		while q:
			brd, i, steps = q.pop()
			if brd == '123450':
				return steps
			for nbr in (-1, 1, col, -col):
				j = i + nbr
				if j < 0 or j >= row*col or not (i//col == j//col or i%col == j%col):
					continue
				l = list(brd)
				l[i], l[j] = l[j], l[i]
				s = ''.join(l)
				if s not in visited:
					visited.add(s)
					q.appendleft((s, j, steps + 1))

		return -1


print(Solution().slidingPuzzle([[3,2,4],[1,5,0]]))