'''
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root == None:
            return []
        ans = [[root.val]]
        if root.children == None:
            return ans
        rq = root.children
        while len(rq) > 0:
            vq = []
            cq = []
            for r in rq:
                vq += [r.val]
                if r.children is not None:
                    cq += r.children
            ans += [vq]
            rq = cq
        return ans
        
