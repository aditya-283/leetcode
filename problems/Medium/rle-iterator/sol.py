from typing import List

class RLEIterator:

	def __init__(self, encoding: List[int]):
		self.pointer = 0
		self.encoding = encoding

	def next(self, n: int) -> int:
		if self.pointer >= len(self.encoding):
			return -1
		while n > self.encoding[self.pointer]:
			n -= self.encoding[self.pointer]
			self.pointer += 2
			if self.pointer >= len(self.encoding):
				return -1
		self.encoding[self.pointer] -= n
		ans = self.encoding[self.pointer+1]
		return ans

