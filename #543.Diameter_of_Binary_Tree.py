'''
https://leetcode.com/problems/diameter-of-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        global maxl
        maxl = 0
        def _getm(tn):
            global maxl
            if tn == None:
                return 0
            tl,tr = _getm(tn.left),_getm(tn.right)
            maxl = max(maxl,tl+tr)
            return max(tl,tr)+1
        _getm(root)
        return maxl
            
        
