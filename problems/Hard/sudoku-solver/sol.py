from typing import List
import copy

class Solution:
	def solveSudoku(self, board: List[List[str]]) -> None:
		return self.sudokuHelper(board, {})

	def sudokuHelper(self, board, visited):
		def conflicting(visited, board, i, j):
			new_board = copy.deepcopy(board)
			for r, c in visited:
				new_board[r][c] = visited[(r, c)]

			rotated = list(list(row) for row in zip(*new_board))

			columnEntries = {int(x) for x in rotated[j] if x != '.'}
			rowEntries = {int(x) for x in new_board[i] if x != '.'}

			squareEntries = set()
			for r in range(i - (i % 3), i - (i % 3) + 3):
				for c in range(j - (j % 3), j - (j % 3) + 3):
					if new_board[r][c] != '.':
						squareEntries.add(int(new_board[r][c]))

			return rowEntries.union(columnEntries).union(squareEntries)


		for i in range(9):
			for j in range(9):
				if board[i][j] != '.' or (i, j) in visited:
					continue

				valid_choices = set(range(1, 10)) - conflicting(visited, board, i, j)
				return any([self.sudokuHelper(board, visited | {(i, j) : choice}) for choice in valid_choices]) if valid_choices else False

		for i, j in visited:
			board[i][j] = str(visited[(i, j)])
		return True


Solution().solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]])
# Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]])





