from collections import deque, defaultdict


def create_adjlist(edges):
	adjlist = defaultdict(list)
	for f, t in edges:
		adjlist[f].append(t)
		if t not in adjlist:
			adjlist[t] = []
	return adjlist


def topo(adjlist):
	def dfs_visit(s):
		opened.add(s)
		for nbr in adjlist[s]:
			if nbr not in opened and nbr not in finished:
				if not dfs_visit(nbr):
					return False
			elif nbr in opened:
				ancestors = list(opened)
				# print('Cycle is ', ancestors[ancestors.index(nbr):] + [nbr])
				return False
		opened.remove(s)
		finished.add(s)
		topo.appendleft(s)
		return True

	opened, finished, topo = set(), set(), deque()
	for v in adjlist.keys():
		if v not in finished:
			if not dfs_visit(v):
				# print('Topological sorting not possible')
				return 
	return list(topo)




print(topo(create_adjlist([[1, 2], [1, 3], [2, 3], [3, 4], [4, 6], [3, 5], [6, 2]])))


# revolutionary idea
# ZIP TO LOOK AT PAIRS
# THIS CHANGES EVERYTHING.