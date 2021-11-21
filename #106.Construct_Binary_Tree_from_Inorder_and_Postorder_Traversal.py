'''
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def _c(io,po):
            if len(io) == 0:
                return None
            root = TreeNode(val=po[-1])
            ind_io = io.index(po[-1])
            iol,ior = io[:ind_io],io[ind_io+1:]
            pol,por = po[:len(iol)],po[len(iol):-1]
            root.left = _c(iol,pol)
            root.right = _c(ior,por)
            return root
        return _c(inorder,postorder)
            
