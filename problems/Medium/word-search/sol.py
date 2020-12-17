from typing import List
class Solution:
	def existsFrom(self, board, word, i, j):
			if not word:
				return True

			if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[0]:
				return False


			tmp, board[i][j] = board[i][j], '#'
			doesExist =  self.existsFrom(board, word[1:], i+1, j) \
						or self.existsFrom(board, word[1:], i-1, j) \
						or self.existsFrom(board, word[1:], i, j-1) \
						or self.existsFrom(board, word[1:], i, j+1) 
			board[i][j] = tmp
			return doesExist

	def exist(self, board: List[List[str]], word: str) -> bool:
		for i in range(len(board)):
			for j in range(len(board[0])):
				if self.existsFrom(board, word, i, j):
					return True
		return False


print(Solution().exist(board=[["A","B","C","E"],
							  ["S","F","E","S"],
							  ["A","D","E","E"]], word="ABCESEEEFS"))
