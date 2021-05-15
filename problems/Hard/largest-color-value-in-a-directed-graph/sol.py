from typing import List
from collections import defaultdict, Counter, deque
from functools import cache

class Solution:
	def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
		n = len(colors)
		adjlist = [set() for _ in range(n)]
		indegree = defaultdict(int)
		for u, v in edges:
			if u == v:
				return -1
			adjlist[u].add(v)
			indegree[v] += 1

		opened, finished, topo = set(), set(), deque()
		dp = {i: defaultdict(int) for i in range(n)}
		def dfs(s):
			opened.add(s)
			dp[s][colors[s]] += 1
			for nbr in adjlist[s]:
				if nbr in opened and nbr not in finished:
					return False
				if nbr not in opened:
					for k in dp[s]:
						dp[nbr][k] = max(dp[nbr][k], dp[s][k])
					indegree[nbr] -= 1
					if indegree[nbr] == 0:
						if not dfs(nbr):
							return False

			finished.add(s)
			topo.appendleft(s)
			return True

		src = [node for node in range(n) if indegree[node] == 0]
		if not src:
			return -1
		if not all(dfs(s) for s in src if s not in opened):
			return -1

		if len(opened) < n:
			return -1

		ans = 0
		for k in dp:
			for c in dp[k]:
				ans = max(ans, dp[k][c])

		return ans


# print(Solution().largestPathValue("a"*9, [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]))
print(Solution().largestPathValue("aaa", [[1,2],[2,1]]))