'''
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def checkgood(node, mv):
            if node == None:
                return 0
            mv = max(mv, node.val)
            if mv == node.val:
                curgood = 1
            else:
                curgood = 0
            return curgood + checkgood(node.left, mv) + checkgood(node.right, mv)
        return checkgood(root, root.val)
        
