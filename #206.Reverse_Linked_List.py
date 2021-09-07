'''
https://leetcode.com/problems/reverse-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def _r(ListNode):
            if ListNode.next == None:
                return ListNode,ListNode
            else:
                h,t = _r(ListNode.next)
                ListNode.next = None
                t.next = ListNode
                return h,ListNode
        if head == None:
            return None
        return _r(head)[0]
                
