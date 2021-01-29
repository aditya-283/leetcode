from typing import List
from collections import defaultdict
from heapq import heappush, heappop, heapreplace, nlargest
class Solution:
	def topKFrequent(self, nums: List[int], k: int) -> List[int]:
		return [x[1] for x in nlargest(k, [(value, key) for key, value in Counter(nums).items()])]


print(Solution().)