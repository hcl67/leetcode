'''
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        #方法1，把bst变成list
        def bst2lst(TreeNode):
            if TreeNode is None:
                return []
            else:
                return bst2lst(TreeNode.left)+[TreeNode.val]+bst2lst(TreeNode.right)
        lst = bst2lst(root)
        i = 0
        j = len(lst)-1
        while i<j:
            if lst[i]+lst[j] == k:
                return True
            elif lst[i] + lst[j] > k:
                j -= 1
            else:
                i += 1
        return False
        
