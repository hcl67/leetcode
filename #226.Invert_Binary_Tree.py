'''
https://leetcode.com/problems/invert-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def _it(tn):
            if tn != None:
                tn.left,tn.right = tn.right,tn.left
                _it(tn.left)
                _it(tn.right)
        _it(root)
        return root
        
