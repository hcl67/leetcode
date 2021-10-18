'''
https://leetcode.com/problems/cousins-in-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if root.val in {x,y}:
            return False
        queue = [root]
        flag = 0
        while flag == 0:
            newqueue= []
            for tn in queue:
                if tn.left != None and tn.right != None and tn.left.val in {x,y} and tn.right.val in {x,y}:
                    return False
                if tn.left != None:
                    newqueue += [tn.left]
                    if tn.left.val in {x,y}:
                        flag += 1
                if tn.right != None:
                    newqueue += [tn.right]
                    if tn.right.val in {x,y}:
                        flag += 1
            if flag == 1:
                return False
            if flag == 2:
                return True
            queue = newqueue
                    
        
