#never use, all-paths is O(n^2) and is almost never useful or necessary. Nevertheless this computation CAN be done and is not too exorbitant.
from functools import cache
from collections import defaultdict
from itertools import chain

def concat(*args):
	return [x for arg in args for x in arg]

def flatten(nested):
	ans = []
	for l in nested:
		if isinstance(l, (int, str)):
			ans.append(l)
		elif isinstance(l, list):
			ans.extend(flatten(l))
	return ans

def allPaths(edges):
	@cache
	def dfs(s):
		opened.add(s)
		paths = []
		for nbr in adjlist[s]:
			if nbr in opened and nbr not in finished:
				print('Cycle detected')
				raise ValueError("Cycle detected!")
			if nbr in finished or nbr not in opened:
				paths.extend(dfs(nbr))
		finished.add(s)
		return [str(s) + ' ' + path for path in paths] if paths else [str(s)]


	adjlist, incident, nodes = defaultdict(list), defaultdict(list), set()
	for u, v in edges:
		adjlist[u].append(v)
		incident[v].append(u)
		nodes.add(u); nodes.add(v)

	src = [node for node in nodes if node not in incident]
	opened, finished, paths = set(), set(), []
	print(src)
	try:
		return flatten(dfs(s) for s in src) if src else -1
	except ValueError:
		return -1


print(allPaths([[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]))
