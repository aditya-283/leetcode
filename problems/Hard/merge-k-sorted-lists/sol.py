# Definition for singly-linked list.
from typing import List

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		if self.next:
			return f'{self.val} {self.next}'
		else:
			return f'{self.val}'

from heapq import heapify, heappop, heappush

class Solution:
	def mergeKLists(self, lists):
		vals = [(head.val, i) for i, head in enumerate(lists) if head is not None]
		heapify(vals)
		cur, first = None, None
		while any(lists):
			next = heappop(vals)[1]
			if lists[next].next:
				heappush(vals, ((lists[next].next.val), next))
			if cur is None:
				first = lists[next]
				cur = first
			else:
				cur.next = lists[next]
				cur = cur.next
			lists[next] = lists[next].next
		return first


# lists = [[1,4,5],[1,3,4],[2,6]]
lists = [ListNode(1, ListNode(4, ListNode(5))),
		 ListNode(1, ListNode(3, ListNode(4))), 
		 ListNode(2, ListNode(6))]

print(Solution().mergeKLists(lists))
# print(Solution().reverseTCO(ListNode(1, ListNode(4, ListNode(5))), None))