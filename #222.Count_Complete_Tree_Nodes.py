'''
https://leetcode.com/problems/count-complete-tree-nodes/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def _cntlf(tn,d):
            r = 0
            if tn == None:
                return r
            elif d == 'left':
                while tn.left != None:
                    r += 1
                    tn = tn.left
                return r
            elif d == 'right':
                while tn.right != None:
                    r += 1
                    tn = tn.right
                return r
        def _cntbh(tn):
            if tn == None:
                return 0
            elif tn.left == None:
                return 1
            elif tn.right == None:
                return 2
            cl = _cntlf(tn,"left")
            cr = _cntlf(tn,"right")
            if cl == cr:
                return 2**(cl+1)-1
            else:
                clr = _cntlf(tn.left,"right") 
                if clr == cl-1:
                    return 2**(cl)+_cntbh(tn.right)
                else:
                    return 2**(cr)+_cntbh(tn.left)
        return _cntbh(root)
