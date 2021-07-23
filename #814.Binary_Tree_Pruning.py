'''
https://leetcode.com/problems/binary-tree-pruning/
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        def getsubtreemax(tn):
            lmax = rmax = 0

            if tn.right is not None:
                rmax = getsubtreemax(tn.right)
                if rmax == 0:
                    tn.right = None
            if tn.left is not None:
                lmax = getsubtreemax(tn.left)
                if lmax == 0:
                    tn.left = None
            return max(tn.val,lmax,rmax)
        
        rootval = getsubtreemax(root)
        if rootval == 0:
            return
        else:
            return root
