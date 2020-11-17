# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		if self.next:
			return f'{self.val} {self.next}'
		else:
			return f'{self.val}'

class Solution:
	def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
		if l1 is None:
			return l2
		elif l2 is None:
			return l1
		elif l1.val < l2.val:
			l1.next = self.mergeTwoLists(l1.next, l2)
			return l1
		else:
			l2.next = self.mergeTwoLists(l1, l2.next)
			return l2

l1 = ListNode(1, ListNode(3, ListNode(5, ListNode(7))))
l2 = ListNode(2, ListNode(4, ListNode(6, ListNode(6.5, ListNode(8)))))

# print(l1)
# print(l2)

print(Solution().mergeTwoLists(l1, l2))