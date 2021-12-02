'''
https://leetcode.com/problems/odd-even-linked-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None or head.next.next == None:
            return head
        ind = 1
        cur = head.next.next
        oddhead = head
        oddtail = head
        evenhead = head.next
        eventail = head.next
        eventail.next = None
        while cur != None:
            if ind == 0:
                eventail.next = cur
                eventail = cur
                cur = cur.next
                eventail.next = None
            else:
                oddtail.next = cur
                oddtail = cur
                cur = cur.next
                oddtail.next = evenhead
            ind = (ind + 1) % 2
        return oddhead
