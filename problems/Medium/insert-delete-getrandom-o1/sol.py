from typing import List
from random import choice


class RandomizedSet:

	def __init__(self):
		self.keys = {}
		self.values = []

	def insert(self, val: int) -> bool:
		if val not in self.keys:
			self.values.append(val)
			self.keys[val] = len(self.values)-1
			return True
		else:
			return False


	def remove(self, val: int) -> bool:
		n = len(self.values)
		if val in self.keys:
			idx = self.keys.pop(val)
			if idx < n-1:
				self.values[idx], self.values[n-1] = self.values[n-1], self.values[idx]
				self.keys[self.values[idx]] = idx
			self.values.pop()
			return True
		else:
			return False
		

	def getRandom(self) -> int:
		return choice(self.values)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()