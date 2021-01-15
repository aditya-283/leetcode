from typing import List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
    	if not preorder or not inorder:
    		return None

    	rootIdxInorder = inorder.index(preorder[0])
    	rightSubtreeSize = len(inorder) - inorder.index(preorder[0]) - 1
    	leftSubtreeSize = inorder.index(preorder[0])

    	return TreeNode(preorder[0], 
    		            self.buildTree(preorder[1:leftSubtreeSize+1], inorder[:rootIdxInorder]), 
    				    self.buildTree(preorder[-rightSubtreeSize:], inorder[rootIdxInorder+1:]))

a = Solution().buildTree([3,9,20,15,7], [9,3,15,20,7])
print(a.right.right.val)