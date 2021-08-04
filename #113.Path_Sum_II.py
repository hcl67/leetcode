'''
https://leetcode.com/problems/path-sum-ii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        if root == None:
            return []
        ans = []
        def getPath(tn):
            r = []
            if tn.left is not None:
                r += [[tn.val] + l for l in getPath(tn.left)]
            if tn.right is not None:
                r += [[tn.val] + r for r in getPath(tn.right)]
            if len(r) == 0:
                r = [[tn.val]]
            return r
        pathq = getPath(root)
        for p in pathq:
            if sum(p) == targetSum:
                ans += [p]
        return ans
            
                
            
        
        
