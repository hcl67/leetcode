'''
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def findx(node, x):
#            print(node.val)
            if node == x:
                return [node]
            if node.left is not None:
                pathl = findx(node.left, x)
                if len(pathl) > 0:
                    return [node] + pathl
            if node.right is not None:
                pathr = findx(node.right, x)
                if len(pathr) > 0:
                    return [node] + pathr
            return []
        pathp = findx(root, p)
        if q in pathp:
            return q
        pathq = findx(root, q)     
        if p in pathq:
            return p
        for i in range(1, min(len(pathp), len(pathq))):
            if pathp[i] != pathq[i]:
                return pathp[i-1]
        
