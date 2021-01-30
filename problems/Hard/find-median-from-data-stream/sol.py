from typing import List
from heapq import heappush, heappop

class MedianFinder:
	def __init__(self):
		self.left_max_heap = []
		self.right_min_heap = []
		self.middle = None # only if odd number of elements

	def addNum(self, num: int) -> None:
		if self.middle is not None and num < self.middle:
			heappush(self.left_max_heap, -num)
			heappush(self.right_min_heap, self.middle)
			self.middle = None
		elif self.middle is not None and num >= self.middle:
			heappush(self.left_max_heap, -self.middle)
			heappush(self.right_min_heap, num)
			self.middle = None
		elif not self.left_max_heap:
			self.middle = num
		elif num < -self.left_max_heap[0]:
			self.middle = -heappop(self.left_max_heap)
			heappush(self.left_max_heap, -num)
		elif num < self.right_min_heap[0]:
			self.middle = num
		else:
			self.middle = heappop(self.right_min_heap)
			heappush(self.right_min_heap, num)


	def findMedian(self) -> float:
		if self.middle:
			return self.middle
		else:
			return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2
		


		

# BITCH BE CAREFUL WITH EDGECASES
# NEW GOAL - DONT LOOK AT THE TEST CASE THAT FAILED.


# Your MedianFinder object will be instantiated and called as such:
obj = MedianFinder()
obj.addNum(40)
ans1 = obj.findMedian()
obj.addNum(12)
print(obj.left_max_heap, '--', obj.middle, '--', obj.right_min_heap)
ans2 = obj.findMedian()
obj.addNum(16)
print(obj.left_max_heap, '--', obj.middle, '--', obj.right_min_heap)
ans3 = obj.findMedian()
print(obj.left_max_heap, '--', obj.middle, '--', obj.right_min_heap)
print(ans3)

