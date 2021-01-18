from typing import List
from collections import defaultdict
from random import randrange
from timeit import repeat

class Set:
	def __repr__(self):
		if self.parent != self:
			return f'{self.parent}'
		else:
			return f'SET[repr: {self.val}, rank: {self.rank}]'

	def __init__(self, x):
		self.val = x
		self.rank = 0
		self.parent = self

class DisjointSetForest:
	def __init__(self, lst: List[int]):
		self.data = lst
		self.map = {x: Set(x) for x in lst}

	def __repr__(self):
		return '\n'.join([f'{x} in set {self.find_set(self.map[x])}' for x in self.data])

	def find_set(self, y: Set):
		if y.parent != y:
			y.parent = self.find_set(y.parent)
		return y.parent

	def union(self, x: Set, y: Set) -> Set:
		if x.rank < y.rank:
			x.parent = y
			return y
		elif x.rank == y.rank:
			x.parent = y
			y.rank += 1
			return y
		else:
			y.parent = x
			return x

	#### User interface ####

	def find(self, x):
		return self.find_set(self.map[x])

	def link(self, x, y):
		self.union(self.find(x), self.find(y))

class Solution:
	def longestConsecutive(self, nums):
		if not nums:
			return 0
		members = set(nums)
		nums = list(members)
		forest = DisjointSetForest(nums)
		for num in nums:
			if (num-1) in members:
				forest.link(num-1, num)
			if (num+1) in members:
				forest.link(num, num+1)
		counts = defaultdict(int)
		for num in nums:
			counts[forest.find(num)] += 1

		return max(counts.values())


class SolutionSlow:
	def longestConsecutive(self, nums: List[int]) -> int:
		if not nums:
			return 0
		nums = list(set(nums))
		nums.sort()
		consec = [0] * len(nums)
		for i, num in enumerate(nums):
			if num == nums[i-1] + 1:
				consec[i] = 1

		max_count, count = 0, 0
		for x in consec:
			if x == 1:
				count += 1
				max_count = max(max_count, count)
			else:
				count = 0
		# print(nums, consec, max_count)
		return max_count + 1


setup_code = 'from __main__ import Solution; from random import randrange'
stmt = 'Solution().longestConsecutive([randrange(1, 999999) for i in range(1000000)])'
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)
print(min(times))
## 3.5 seconds

setup_code = 'from __main__ import SolutionSlow; from random import randrange'
stmt = 'SolutionSlow().longestConsecutive([randrange(1, 999999) for i in range(1000000)])'
times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=3)
print(min(times))
## 9.3 seconds


# forest = DisjointSetForest([1, 2, 3, 4, 5])
# forest.link(2, 3)
# forest.link(4, 5)
# forest.link(2, 4)
# print(forest)
# print(forest.find(1))

