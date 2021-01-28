from typing import List
from heapq import heappush, heappop
# class Solution:
# 	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
# 		def intersects(interval1, interval2):
# 			start1, end1 = interval1
# 			start2, end2 = interval2
# 			return start2 <= start1 < end2 or start2 < end1 <= end2 or \
# 				start1 <= start2 < end1 or start1 < end2 <= end1 


# 		pq = []
# 		intervals.sort()
# 		count, ans = 1, 1
# 		for interval in intervals:
# 			if not pq:
# 				count = 1
# 				heappush(pq, (interval[1], interval))
# 				continue

# 			if intersects(interval, pq[0][1]):
# 				count += 1
# 				ans = max(ans, count)
# 				heappush(pq, (interval[1], interval))
# 			else:
# 				heappop(pq)
# 				heappush(pq, (interval[1], interval))

# 		return ans


class Solution:
	def minMeetingRooms(self, intervals: List[List[int]]) -> int:
		pq = []
		for x, y in intervals: 
			heappush(pq, (x, +1))
			heappush(pq, (y, -1))
			
		ans = prefix = 0
		while pq: 
			_, x = heappop(pq)
			prefix += x
			ans = max(ans, prefix)
		return ans 

print(Solution().minMeetingRooms([[6,17],[8,9],[11,12],[6,9]]))
print(Solution().minMeetingRooms([[15,16],[10,15],[16,25]]))