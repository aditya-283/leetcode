from typing import List

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    # def __repr__(self):
    	# return f'{self.val}-{self.right}'

class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
    	if not root:
    		return None
    	leftHead, rightHead, leftmost, rightmost = None, None, None, None
    	if root.left:
    		leftHead = self.treeToDoublyList(root.left)
    		if leftHead.left:
    			root.left = leftHead.left
    			leftHead.left.right = root
    		else:
    			leftHead.right = root
    	if root.right:
    		rightHead = self.treeToDoublyList(root.right)
    		if rightHead.left:
    			leftHead.left = rightHead.left
    			rightHead.left.right = leftHead
    		else:
    			leftHead.left = rightHead
    			rightHead.right = leftHead
    		rightHead.left = root
    		root.right = rightHead
    	return leftHead or root


# print(Solution().treeToDoublyList(Node(2, Node(1), Node(3))).left.val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).right.val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).right.right.val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).right.right.right.val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).right.right.right.right.val)
print(Solution().treeToDoublyList(Node(4, Node(2, Node(1), Node(3)), Node(5))).right.right.right.right.right.val)