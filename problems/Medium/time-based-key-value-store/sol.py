from typing import List
from bisect import bisect_right
from collections import defaultdict
from math import inf

class TimeMap:
	def __init__(self):
		self.timeMap = defaultdict(list)
		
	def set(self, key: str, value: str, timestamp: int) -> None:
		self.timeMap[key].append((timestamp, value))

	def get(self, key: str, timestamp: int) -> str:
		if key in self.timeMap:
			idx = bisect_right(self.timeMap[key], (timestamp, 'z'))
			if idx == 0:
				return ""
			else:
				return self.timeMap[key][idx-1][1]
		else:
			return ""

test = TimeMap()
test.set("foo", "bar" , 1)
print(test.get("foo", 1))