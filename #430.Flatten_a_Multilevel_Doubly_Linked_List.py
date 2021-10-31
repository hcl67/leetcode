'''
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
'''
"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        def _c(head):
            cur = head
            while 1:
                if cur.child != None:
                    childtail = _c(cur.child)
                    if cur.next != None:
                        cur.next.prev = childtail
                        childtail.next = cur.next
                    cur.child.prev = cur
                    cur.next = cur.child
                    cur.child = None
                    cur = childtail
                if cur.next == None:
                    break
                else:
                    cur = cur.next
            return cur
        if head != None:
            _c(head)
        return head
        
