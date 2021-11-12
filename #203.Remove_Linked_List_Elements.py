'''
https://leetcode.com/problems/remove-linked-list-elements/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newhead = head
        while newhead != None and newhead.val == val:
            newhead = newhead.next
        pre = newhead
        while pre != None:
            cur = pre.next
            if cur != None and cur.val == val:
                pre.next = cur.next
            else:    
                pre = cur
        return newhead
        
