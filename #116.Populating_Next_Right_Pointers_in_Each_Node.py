'''
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if root == None:
            return root
        q = deque([root,None])
        while q:
            cur = q.popleft()
            if cur == 'Q':
                break
            elif cur == None:
                q.append(None)
            else:
                cur.next = q[0]
                if cur.left == None:
                    q.append('Q')
                else:
                    q.append(cur.left)
                    q.append(cur.right)
        return root
            
        
