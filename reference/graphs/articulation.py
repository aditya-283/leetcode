# Tarjan's algorithm for articulation edges (bridges) and articulation vertices
from math import inf

# assumes a connected graph. if not run outer loop over vertices
def bridges(adjlist):
	def dfs_bridges(time, node, parent):
		disc[node] = time
		low[node] = time
		for nbr in adjlist[node]:
			if nbr == parent:
				continue

			if disc[nbr] != inf:
				low[node] = min(low[node], disc[nbr])
			if disc[nbr] == inf:
				dfs_bridges(time + 1, nbr, node)
				if low[nbr] > disc[node]:
					bridges.append((node, nbr))
				else:
					low[node] = min(low[node], low[nbr])

	n = len(adjlist)
	disc = [inf] * n
	low  = [inf] * n
	bridges = []
	dfs_bridges(0, 1, -1)
	return bridges

# salient points for both - disc array initialised to inf or 0 or something, time passed as param (python quirk), either parent array (overkill imo) or parent passed as param
def articulation_points(adjlist):
	source = 0
	def dfs_ap(time, node, parent):
		disc[node] = time
		low[node] = time
		numEdges = 0
		for nbr in adjlist[node]:
			if nbr == parent:
				continue

			if disc[nbr] != inf:
				low[node] = min(low[node], disc[nbr])
			if disc[nbr] == inf:
				numEdges += 1
				dfs_ap(time + 1, nbr, node)
				if node != source and low[nbr] >= disc[node]: # if we don't do this starting node will always be AP
					ap.append(node)
				else:
					low[node] = min(low[node], low[nbr])

		if node == source and numEdges >= 2:
			ap.append(node) # this checks when starting node is AP. When it has disconnected child subtrees

	n = len(adjlist)
	disc = [inf] * n
	low  = [inf] * n
	ap = []
	dfs_ap(0, 0, -1)
	return list(set(ap))

