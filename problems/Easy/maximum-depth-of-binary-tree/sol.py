from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
    	if not root:
    		return 0
    	else:
    		return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))