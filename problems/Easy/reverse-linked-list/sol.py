from typing import List

# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

class Solution:
	def reverseList(self, head: ListNode) -> ListNode:
		if not head:
			return None
		it = head.next
		first = head
		head.next = None
		while it:
			next = it.next
			it.next = first
			first = it
			it = next
		return first