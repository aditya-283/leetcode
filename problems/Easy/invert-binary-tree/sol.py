from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
        	return

        inverted_right = self.invertTree(root.right)
        inverted_left = self.invertTree(root.left)
        root.right = inverted_left
        root.left = inverted_right
       	return root