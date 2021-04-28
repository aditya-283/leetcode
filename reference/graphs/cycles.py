def isBipartiteBFS(self, graph: List[List[int]]) -> bool:
	def bfsContainsOddCycle(s, step):
		q = deque()
		q.appendleft((s, 0))
		disc.add(s)
		dist[s] = 0
		while q:
			cur, step = q.pop()
			step += 1
			for nbr in graph[cur]:
				if nbr not in disc:
					disc.add(nbr)
					dist[nbr] = step
					parent[nbr] = cur
					q.appendleft((nbr, step))
				elif nbr != parent[cur]:
					print(cur, nbr)
					cycleLen = dist[nbr] + dist[cur] + 1
					if cycleLen % 2:
						print(f'Detected cycle due to edge {cur}-{nbr} with starting node {s}')
						return True
		return False

	disc = set()
	parent = {}
	dist = {}
	return not any(bfsContainsOddCycle(i, 0) for i in range(len(graph)) if i not in disc)


	