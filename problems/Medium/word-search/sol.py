from typing import List
import copy

from typing import List



class Solution:
	def existsFrom(self, board, seen, word, i, j):
			if not word:
				return True

			if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]):
				return False

			if (i, j) not in seen and board[i][j] == word[0]:
				return self.existsFrom(board, [(i, j)] + seen, word[1:], i+1, j) \
						or self.existsFrom(board, [(i, j)] + seen, word[1:], i-1, j) \
						or self.existsFrom(board, [(i, j)] + seen, word[1:], i, j-1) \
						or self.existsFrom(board, [(i, j)] + seen, word[1:], i, j+1) 
			else:
				return False

	def exist(self, board: List[List[str]], word: str) -> bool:
		exists = False
		for i in range(len(board)):
			for j in range(len(board[0])):
				exists |= self.existsFrom(board, [], word, i, j)
				if exists:
					break
		return exists


print(Solution().exist(board=[["A","B","C","E"],
							  ["S","F","E","S"],
							  ["A","D","E","E"]], word="ABCESEEEFS"))
