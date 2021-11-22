'''
https://leetcode.com/problems/delete-node-in-a-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        cur = root
        preroot = TreeNode(left = root)
        pre = preroot
        while cur != None:
            if cur.val == key:
                if cur.left != None:
                    rmright = cur.right
                    cur.val = cur.left.val
                    cur.right = cur.left.right
                    cur.left = cur.left.left
                    while cur.right != None:
                        cur = cur.right
                    cur.right = rmright
                elif cur.right != None:
                    rmleft = cur.left
                    cur.val = cur.right.val
                    cur.left = cur.right.left
                    cur.right = cur.right.right
                    while cur.left != None:
                        cur = cur.left
                    cur.left = rmleft
                else:
                    if pre.left != None and pre.left.val == key:
                        pre.left = None
                    else:
                        pre.right = None
                return preroot.left
            elif cur.val < key:
                pre = cur
                cur = cur.right
            else:
                pre = cur
                cur = cur.left
        return preroot.left
        
