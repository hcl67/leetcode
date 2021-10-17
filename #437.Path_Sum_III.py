'''
https://leetcode.com/problems/path-sum-iii/
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root == None:
            return 0
        '''
        from queue import Queue
        bfs0,bfs1,ans = Queue(),Queue(),0
        bfs0.put(root)
        while not bfs0.empty():
            cur = bfs0.get()
            if cur.left != None:
                bfs0.put(cur.left)
            if cur.right != None:
                bfs0.put(cur.right) 
            bfs1.put((cur.val,cur))
        while not bfs1.empty():
            cur = bfs1.get()
            #print(cur[0],cur[1].val)
            if cur[0] == targetSum:
                ans += 1
            if cur[1].left != None:
                bfs1.put((cur[0]+cur[1].left.val,cur[1].left))
            if cur[1].right != None:
                bfs1.put((cur[0]+cur[1].right.val,cur[1].right))
        return ans
        '''
        from queue import Queue
        dic = {}
        bfs0 = Queue()
        bfs0.put((1,root))
        while not bfs0.empty():
            cur = bfs0.get()
            if cur[1].left != None:
                bfs0.put((cur[0]*2,cur[1].left))
            if cur[1].right != None:
                bfs0.put((cur[0]*2+1,cur[1].right)) 
            dic[cur[0]] = cur[1].val
        ans = 0
        #print(dic)
        for k in dic.keys():
            tk = k
            ts = 0
            while tk>0:
                ts += dic[tk]
                if ts == targetSum:
                    ans += 1
                tk //= 2
        return ans

        
        
