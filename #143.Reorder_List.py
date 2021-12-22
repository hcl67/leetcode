'''
https://leetcode.com/problems/reorder-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        ll = []
        cur = head
        while cur != None:
            ll += [cur]
            cur = cur.next
        n = len(ll)
        if n <= 2:
            return head
        for i in range(n//2):
            ll[i].next = ll[n-1-i]
            ll[n-1-i].next = ll[i+1]
        if n&1:
            ll[i+1].next = None
        else:
            ll[n-1-i].next = None
        return head
        
        
        
        
