from typing import List
import operator

class Solution:
	def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
		def intersects(interval1, interval2):
			start1, end1 = interval1
			start2, end2 = interval2
			return start2 <= start1 < end2 or start2 < end1 <= end2 or \
				start1 <= start2 < end1 or start1 < end2 <= end1 



		intervals.sort(key=operator.itemgetter(1, 0))
		first = True
		for interval in intervals:
			if first:
				first = False
				last = interval
				continue

			if intersects(interval, last):
				return False
			else:
				last = interval
		return True


print(Solution().canAttendMeetings([[1, 1.5], [2, 4]]))