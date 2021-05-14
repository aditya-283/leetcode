from typing import List
from collections import defaultdict, Counter
from functools import cache

class Solution:
	def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
		@cache
		def dfs(s):
			opened.add(s)
			paths = []
			for nbr in adjlist[s]:
				if nbr in opened and nbr not in finished:
					return False
				if nbr in finished:
					paths.extend(dfs(nbr))
				if nbr not in opened:
					ans = dfs(nbr)
					if not ans:
						return False
					else:
						paths.extend(ans)
			finished.add(s)
			return [str(s) + ' ' + path for path in paths] if paths else [str(s)]
		
		if not edges:
			return 1
		adjlist = defaultdict(list)
		incident = defaultdict(list)
		nodes = set()
		for u, v in edges:
			if u == v:
				return -1
			adjlist[u].append(v)
			incident[v].append(u)
			nodes.add(u); nodes.add(v)

		src = [node for node in nodes if node not in incident]
		opened, finished = set(), set()
		paths = []
		if not src:
			return -1
		for s in src:
			ans = dfs(s)
			if not ans:
				return -1
			else:
				paths.extend(ans)
		# print(paths)

		ans = 0
		for path in paths:
			cnt = Counter(colors[int(i)] for i in path.split())
			ans = max(ans, cnt.most_common()[0][1])
		return ans



print(Solution().largestPathValue("bwsswpwbpwpsbswbwswbwbbbwpwsbsssw", [[0,1],[1,2],[2,3],[3,4],[4,5],[3,5],[2,6],[5,7],[6,8],[7,8],[4,9],[8,9],[7,9],[9,10],[8,10],[5,10],[9,11],[10,12],[11,12],[9,12],[12,13],[10,13],[11,13],[8,14],[13,14],[12,14],[14,15],[13,15],[11,15],[10,16],[13,17],[10,17],[12,17],[15,17],[8,18],[17,18],[10,18],[14,19],[10,19],[18,19],[14,20],[18,20],[16,20],[19,20],[20,21],[18,21],[16,22],[21,22],[20,22],[14,23],[22,23],[21,23],[20,23],[18,24],[16,24],[22,24],[21,24],[18,25],[22,25],[21,25],[24,25],[20,25],[25,26],[25,27],[25,28],[27,29],[22,29],[28,29],[23,29],[28,30],[24,31],[28,31],[27,31],[29,32],[28,32],[30,32]]))