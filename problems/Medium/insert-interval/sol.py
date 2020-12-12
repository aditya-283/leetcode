from typing import List
import bisect

def firsts(pairs):
	return list(map(lambda x: x[0], pairs))

def seconds(pairs):
	return list(map(lambda x: x[1], pairs))

class Solution:
	def doesOverlap(self, interval1, interval2):
		return interval2[0] <= interval1[1] <= interval2[1] or \
				interval2[0] <= interval1[0] <= interval2[1]

	def overlapIndices(self, intervals, newInterval):
		first = 1
		start, end = -1, -1
		for i, interval in enumerate(intervals):
			if self.doesOverlap(newInterval, interval) or self.doesOverlap(interval, newInterval):
				if first:
					first = 0
					start, end = i, i
				else:
					end = i
			if interval[0] > newInterval[1]:
				break
		return start, end

	def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
		if not intervals: return [newInterval]
		start, end = self.overlapIndices(intervals, newInterval)
		print(start, end)
		if start > -1:
			mergedInterval = [min(newInterval[0], min(firsts(intervals[start: end + 1]))), 
								max(newInterval[1], max(seconds(intervals[start: end + 1])))]
			return intervals[:start] + [mergedInterval] + intervals[end + 1:] if (end < len(intervals)-1) \
					else intervals[:start] + [mergedInterval]
		else:
			bisect.insort(intervals, newInterval)
			return intervals

intervals = [[1,5]]
print(Solution().insert(intervals, [0,6]))