from typing import List
from collections import deque, defaultdict

class Solution:
	def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
		deps = defaultdict(list)
		for later, first in prerequisites:
			deps[first].append(later)

		started = set()
		finished = set()
		topo = deque()
		def dfsTopo(node):
			started.add(node)
			for nbr in deps[node]:
				if nbr not in started and nbr not in finished and not dfsTopo(nbr):
					return False
				if nbr in started and nbr not in finished:
					return False
			started.remove(node)
			finished.add(node)
			topo.appendleft(node)
			return True

		for node in range(numCourses):
			if node not in started and node not in finished:
				if not dfsTopo(node):
					return []

		return list(topo) 

print(Solution().findOrder(2, []))