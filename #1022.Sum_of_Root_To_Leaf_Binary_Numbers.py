'''
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def _c(self, tn, bn):
            if tn.left == None and tn.right == None:
                self.ans += (bn<<1) + tn.val
                return
            else:
                if tn.left != None:
                    _c(self, tn.left, (bn<<1) + tn.val)
                if tn.right != None:
                    _c(self, tn.right, (bn<<1) + tn.val)
            return
        _c(self, root, 0)
        return self.ans
        
