'''
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        #1 构造一颗包含自己及所有儿子的偏序和
        #2 从根开始找，每次往乘积最大的儿子走，直到儿子都小于当前值为止
        def psum(node):
            s = node.val
            if node.left is not None:
                s+=psum(node.left)
            if node.right is not None:
                s+=psum(node.right)
            node.val = s
            return s
        psum(root)
        ans = 0
        curnode = root
        while 1:
            if curnode.left is not None:
                lps = curnode.left.val * (root.val - curnode.left.val) 
            else:
                lps = 0
            if curnode.right is not None:
                rps = curnode.right.val * (root.val - curnode.right.val)
            else:
                rps = 0
            maxp = max(ans,lps,rps)
            if ans == maxp:
                return ans % (10**9+7)
            elif lps == maxp:
                ans = maxp
                curnode = curnode.left
            else:
                ans = maxp
                curnode = curnode.right
