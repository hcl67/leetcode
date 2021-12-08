'''
https://leetcode.com/problems/binary-tree-tilt/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def _c(tn):
            if tn == None:
                return 0,0
            cl,cr = _c(tn.left),_c(tn.right)
            return tn.val+cl[0]+cr[0],abs(cl[0]-cr[0])+cl[1]+cr[1]
        return _c(root)[1]
