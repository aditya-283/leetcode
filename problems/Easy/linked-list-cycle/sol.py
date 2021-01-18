from typing import List

# Definition for singly-linked list.
class ListNode:
	def __init__(self, x):
		self.val = x
		self.next = None

class Solution:
	def hasCycle2(self, head: ListNode) -> bool:
		visited = set()
		iter = head
		while iter:
			addr = id(iter)
			if addr not in visited:
				visited.add(addr)
				iter = iter.next
			else:
				return True
		return False

	def hasCycle(self, head: ListNode) -> bool:
		first = True
		slow, fast = head, head
		while slow and fast and fast.next:
			if slow == fast and not first:
				return True
			else:
				slow = slow.next
				fast = fast.next.next
			if first:
				first = False
		return False


a = ListNode(1)
b = ListNode(2)
a.next = b
# b.next = a


print(Solution().hasCycle(a))