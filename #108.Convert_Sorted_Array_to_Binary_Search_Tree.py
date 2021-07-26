'''
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def genbst(lst):
            if len(lst) == 0:
                return None
            elif len(lst) == 1:
                return TreeNode(val = lst[0])
            else:
                i = len(lst)//2
                return TreeNode(val = lst[i], left = genbst(lst[:i]), right = genbst(lst[i+1:]))
        return genbst(nums)
            
