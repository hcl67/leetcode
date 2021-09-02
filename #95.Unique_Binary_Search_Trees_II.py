'''
https://leetcode.com/problems/unique-binary-search-trees-ii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        lst = list(range(1,n+1))
        def genTree(lst):
            if len(lst) == 0:
                return [None]
            elif len(lst) == 1:
                return [TreeNode(val = lst[0])]
            else:
                r = []
                for i in range(len(lst)):
                    ltree = genTree(lst[:i])
                    rtree = genTree(lst[i+1:])
                    r += [TreeNode(val = lst[i], left = l, right = r) for l in ltree for r in rtree]
                return r
        return genTree(lst)
                    
                
        
