from typing import List
from collections import defaultdict, deque

class Solution:
	def alienOrder(self, words: List[str]) -> str:
		def topo(adjlist):
			def dfs_visit(s):
				opened.add(s)
				for nbr in adjlist[s]:
					if nbr not in opened and nbr not in finished:
						if not dfs_visit(nbr):
							return False
					elif nbr in opened:
						ancestors = list(opened)
						return False
				opened.remove(s)
				finished.add(s)
				topo.appendleft(s)
				return True

			opened, finished, topo = set(), set(), deque()
			for v in adjlist.keys():
				if v not in finished:
					if not dfs_visit(v):
						return []
			return list(topo)

		adjlist = {c: [] for c in set(''.join(words))}
		for cur, nxt in zip(words, words[1:]):
			if len(cur) > len(nxt) and cur[:len(nxt)] == nxt:
				return ''

			for i, j in zip(cur, nxt):
				if i != j:
					if j not in adjlist[i]:
						adjlist[i].append(j)
					break

		return ''.join(topo(adjlist))

a = Solution()
# print(a.alienOrder(["ac","ab","zc","zb"]))
# print(a.alienOrder(["wrt","wrf","er","ett","rftt"]))
print(a.alienOrder(["wrt","wrf","er","ett","rftt","te"]))
# print(a.alienOrder(["abc","ab"]))
# print(a.alienOrder(["wrt","wrtkj"]))
# print(a.alienOrder(["dvpzu","bq","lwp","akiljwjdu","vnkauhh","ogjgdsfk","tnkmxnj","uvwa","zfe","dvgghw","yeyruhev","xymbbvo","m","n"]))


# BITCH SIMPLIFY
# IF YOU NEED AN ADJLIST FOR TOPO DONT MAKE AN EDGELIST FIRST AND THEN CONVERT
# MINIMISE CODE. SIMPLIFYYYYY 
# FUNCTIONS ONLY MAKE SENSE IF THERE REALLY IS MODULARITY REQD. DONT OVERDO FUNCTIONS.