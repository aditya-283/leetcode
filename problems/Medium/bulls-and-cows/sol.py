from typing import List
from collections import defaultdict

class Solution:
	def getHint(self, secret: str, guess: str) -> str:
		bull_indices = set()
		for i, (s, g) in enumerate(zip(secret, guess)):
			if s == g:
				bull_indices.add(i)

		non_bull_guess_chars = defaultdict(int)
		for i, c in enumerate(guess):
			if i not in bull_indices:
				non_bull_guess_chars[c] += 1

		cows = 0
		for i, c in enumerate(secret):
			if i not in bull_indices and c in non_bull_guess_chars and non_bull_guess_chars[c] > 0:
				non_bull_guess_chars[c] -= 1
				cows += 1

		return f"{len(bull_indices)}A{cows}B"

print(Solution().getHint(secret = "1", guess = "1"))