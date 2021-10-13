'''
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        root = TreeNode(preorder[0])
        for i in preorder[1:]:
            cur = root
            while 1:
                if i < cur.val:
                    if cur.left == None:
                        cur.left = TreeNode(i)
                        break
                    else:
                        cur = cur.left
                else:
                    if cur.right == None:
                        cur.right = TreeNode(i)
                        break
                    else:
                        cur = cur.right
        return root
                
        
