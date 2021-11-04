'''
https://leetcode.com/problems/sum-of-left-leaves/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def _s(tn):
            if tn == None:
                return 0
            elif tn.left != None and tn.left.left == None and tn.left.right == None:
                return tn.left.val + _s(tn.right)
            else:
                return _s(tn.left) + _s(tn.right)
        return _s(root)
        
