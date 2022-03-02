'''
https://leetcode.com/problems/binary-tree-maximum-path-sum/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.r = -inf
        @cache
        def _c(self, node):
            if node == None:
                return -inf
            else:
                rl = _c(self,node.left)
                rr = _c(self,node.right)
                t = max(rl + node.val
                       ,rr + node.val
                       ,node.val)
                self.r = max(self.r
                             , rl + rr + node.val
                             , t)
                return t
        _c(self,root)
        return self.r
        
