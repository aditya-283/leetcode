# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

	def __repr__(self):
		if self.next is None:
			return f'{self.val}'
		else:
			return f'{self.val} {self.next}'

def length(head: ListNode) -> int:
	if head is None:
		return 0
	else:
		return 1 + length(head.next)

def removeNthFromStart(head: ListNode, n: int) -> ListNode:
	if n <= 0:
		return DataError('Bad Argument!')
	if n == 1:
		return head.next
	else:
		head.next = removeNthFromStart(head.next, n-1)
		return head


class Solution:
	def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
		return removeNthFromStart(head, length(head) - n + 1) 

l = ListNode(1)
# print(l)
# print(removeNthFromStart(l, 4))
# print(l)
print(Solution().removeNthFromEnd(l, 1))