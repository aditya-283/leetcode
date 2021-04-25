from typing import List
from collections import deque

class Solution:
	def isBipartite(self, graph: List[List[int]]) -> bool:
		def depthFromRoot(x, root):
			l = 0
			while x != root:
				p = parent[x]
				x = p
				l += 1
			return l

		def containsOddCycle(s):
			discovered.add(s)
			parent[s] = -1
			q = deque()
			q.appendleft(s)
			while q:
				cur = q.pop()
				for nbr in graph[cur]:
					if nbr not in discovered:
						parent[nbr] = cur
						discovered.add(nbr)
						q.appendleft(nbr)
					elif nbr != parent[cur]:
						if (depthFromRoot(cur, s) + depthFromRoot(nbr, s) + 1) % 2:
							return True
			return False

		discovered = set()
		parent = {}
		return not any(containsOddCycle(i) for i in range(len(graph)) if i not in discovered)

print(Solution().isBipartite([[1,2,3],[0,2],[0,1,3],[0,2]]))

from typing import List
