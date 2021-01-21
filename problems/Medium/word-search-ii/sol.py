from typing import List

class Solution:
	def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
		def nbrs(i, j):
			return [(r, c) for r, c in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)] if 0 <= r < R and 0 <= c < C]

		def visit(i, j, word, used):
			if word[0] == board[i][j]:
				# print(word, i, j)
				valid_nbrs = [nbr for nbr in nbrs(i, j) if nbr not in used]
				if not word[1:]:
					return True
				return any([visit(r, c, word[1:], [(i, j)] + used) for r, c in valid_nbrs])
			else:
				return False


		R = len(board)
		C = len(board[0])
		present = set()		
		for r in range(R):
			for c in range(C):
				for word in words:
					if word[0] == board[r][c] and word not in present and visit(r, c, word, []):
						present.add(word)
		return list(present)


print(Solution().findWords([["o","a","a","n"], 
							["e","t","a","e"], 
							["i","h","k","r"], 
							["i","f","l","v"]], words = ["oath","pea","eat","rain"]))


print(Solution().findWords([["a", "a"]], words = ["aaa"]))


print(Solution().findWords([["a","b","c"],
							["a","e","d"],
							["a","f","g"]], 
							# words=["eaabcdgfa"]))
							words=["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]))



