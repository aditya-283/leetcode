from typing import List
from collections import deque

class Solution:
	def solve(self, board: List[List[str]]) -> None:
		def nbrs(i, j):
			return [(r, c) for r, c in [(i+1, j),  (i-1, j), (i, j+1), (i, j-1)] if 0 <= r < R and \
																					0 <= c < C and \
																					board[r][c] == 'O']

		def bfs(s):
			visited.add(s)
			q = deque([s])
			while q:
				cur = q.pop()
				for nbr in nbrs(*cur):
					if nbr not in visited:
						visited.add(nbr)
						q.appendleft(nbr)

		visited = set()
		R, C = len(board), len(board[0])
		for i in range(R):
			for j in range(C):
				if (i == 0 or i == R-1 or j == 0 or j == C-1) and board[i][j] == 'O':
					#boundary O
					bfs((i, j))

		for i in range(R):
			for j in range(C):
				if board[i][j] == 'O' and (i, j) not in visited:
					board[i][j] = 'X'

		for row in board:
			print(row)

		return board


Solution().solve([["X","X","X","X"],
				  ["X","O","O","X"],
				  ["X","X","O","X"],
				  ["X","O","X","X"]])

# [["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","X","X","X"],
#  ["X","O","X","X"]]		