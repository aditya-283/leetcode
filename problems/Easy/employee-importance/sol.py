from typing import List

class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class TreeNode:
    def __init__(self, val, children):
        self.val = val
        self.children = children
        
class Solution:
    def getImportance(self, employees, id: int) -> int:
        def findSubtreeSum(root):
            if not root:
                return 0
            else:
                return root.val + sum(findSubtreeSum(node[child]) for child in root.children)
            
        node = {}
        for employee in employees:
            node[employee.id] = TreeNode(employee.importance, employee.subordinates)
            
        return findSubtreeSum(node[id])

