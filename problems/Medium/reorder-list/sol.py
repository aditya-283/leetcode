from typing import List
from collections import deque

class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		return f'{self.val}-{self.next}' if self.next else f'{self.val}'

class SolutionBad:
	def reorderList(self, head: ListNode) -> None:
		# Uses O(n) extra memory. O(n) time
		if not head:
			return None
		iter = head
		nodes = deque()
		while iter:
			nodes.append(iter)
			iter = iter.next

		iter = head
		while iter and nodes:
			last = nodes[-1]
			if iter == last:
				break
			last.next = iter.next
			iter.next = last
			iter = last.next
			nodes.pop()
			nodes.popleft()
		iter.next = None
		return head

# split in half, reverse other half, merge
# write easily readable and debuggable code
# SIMPLIFY SIMPLIFY SIMPLIFY before you implement
class Solution:
	def split(self, head: ListNode) -> ListNode:
		slow, fast = head, head
		while fast and fast.next:
			slow = slow.next
			fast = fast.next.next
		next = slow.next
		slow.next = None
		return next

	def reverse(self, head: ListNode) -> ListNode:
		if not head or not head.next:
			return head
		it = head.next
		head.next = None
		first = head
		while it:
			next = it.next
			it.next = first
			first = it
			it = next
		return first


	def merge(self, head1: ListNode, head2: ListNode) -> ListNode:
		it1, it2 = head1, head2
		last = it1
		while it1 and it2:
			next1, next2 = it1.next, it2.next
			it1.next = it2
			it2.next = next1
			it1 = next1
			it2 = next2
		return head1
			

	def reorderList(self, head: ListNode) -> None:
		if not head:
			return None
		second_half = self.split(head)
		reverse_second_half = self.reverse(second_half)
		return self.merge(head, reverse_second_half)

print(Solution().reorderList(None))
print(Solution().reorderList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
		
# a = 
# # b = ListNode(5, ListNode(4))
# Solution().reorderList(a)





