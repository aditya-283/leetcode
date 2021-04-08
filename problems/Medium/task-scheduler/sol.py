from typing import List
from collections import Counter

class Solution:
	def leastInterval(self, tasks: List[str], n: int) -> int:
		counter = Counter(tasks)
		_, max_count = counter.most_common(1)[0]
		mostFrequent = [x for x, c in counter.items() if c == max_count]
		return max((max_count - 1)*(n+1) + len(mostFrequent), len(tasks))



# class Solution:
# 	def leastInterval(self, tasks: List[str], n: int) -> int:
# 		counter = Counter(tasks)
# 		total_task_count = sum(counter.values())
# 		most_common, max_count = counter.most_common(1)[0]

# 		del counter[most_common]
# 		idles = 0
# 		for i in range(max_count-1):
# 			keys = list(counter.keys())

# 			if len(keys) < n:
# 				idles += n - len(keys)

# 			for k in range(min(len(keys), n)):
# 				counter[keys[k]] -= 1
# 				if counter[keys[k]] == 0:
# 					del counter[keys[k]]

# 		return n*(max_count-1) + max_count + sum(counter.values())

print(Solution().leastInterval(["A","A","A","B","B","B"], 2))
