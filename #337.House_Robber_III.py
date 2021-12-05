'''
https://leetcode.com/problems/house-robber-iii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def _c(tn):
            if tn == None:
                return 0
            else:
                ans1,ans2 = 0,tn.val
                if tn.left != None:
                    ans1 += _c(tn.left)
                    ans2 += _c(tn.left.left) + _c(tn.left.right)
                if tn.right != None:
                    ans1 += _c(tn.right)
                    ans2 += _c(tn.right.left) + _c(tn.right.right)
                return max(ans1,ans2)
        return _c(root)
                    
                
        
