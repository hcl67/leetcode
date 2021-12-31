'''
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        global ans
        ans = 0
        def _c(lst,tn):
            global ans
            if lst:
                ans = max(ans,max(abs(tn.val - i) for i in lst))
            if tn.left != None:
                _c(lst+[tn.val],tn.left)
            if tn.right != None:
                _c(lst+[tn.val],tn.right)
            return
        _c([],root)
        return ans
                
 #实际上只需要传最大最小值就行了，进一步只要求每支的最大最小值       
