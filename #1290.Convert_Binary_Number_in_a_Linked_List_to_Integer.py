'''
https://leetcode.com/problems/convert-binary-number-in-a-linked-list-to-integer/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        cur,ans = head,0
        while (cur!=None):
            ans *= 2
            ans += cur.val
            cur = cur.next
        return ans
        
