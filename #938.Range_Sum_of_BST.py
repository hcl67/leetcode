'''
https://leetcode.com/problems/range-sum-of-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def _c(tn):
            if tn == None:
                return 0
            if tn.val < low:
                return _c(tn.right)
            if tn.val > high:
                return _c(tn.left)
            return tn.val + _c(tn.left) + _c(tn.right)
        return _c(root)
