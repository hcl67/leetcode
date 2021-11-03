'''
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def _s(tn,val):
            if tn.left == None and tn.right == None:
                return val*10+tn.val
            else:
                r = 0
                if tn.left != None:
                    r += _s(tn.left,val*10+tn.val)
                if tn.right != None:
                    r += _s(tn.right,val*10+tn.val)
                return r
        return _s(root,0)
                
        
