from typing import List
from bisect import bisect_left
from sortedcontainers import SortedList

class MyCalendar:
	def __init__(self):
		self.events = SortedList()

	def book(self, start: int, end: int) -> bool:
		idx = bisect_left(self.events, (start, end))
		if idx > 0 and self.events[idx-1][1] > start:
			return False
		elif idx < len(self.events) and self.events[idx][0] < end:
			return False
		self.events.add((start, end))
		return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendar()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20, 30))