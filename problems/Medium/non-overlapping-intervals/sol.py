from typing import List
import operator

class Solution:
	def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
		def doesOverlap(interval1, interval2):
			start1, end1 = interval1
			start2, end2 = interval2
			return start2 <= start1 < end2 or start2 < end1 <= end2 or \
					start1 <= start2 < end1 or start1 < end2 <= end1

		count = 0
		first = True
		intervals.sort(key=operator.itemgetter(1, 0))
		for interval in intervals:
			if first:
				last = interval
				first = False
			elif not first and doesOverlap(interval, last):
				count += 1
			else:
				last = interval

		return count

print(Solution().eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]))