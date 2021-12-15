'''
https://leetcode.com/problems/insertion-sort-list/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sorthead = ListNode(val=head.val)
        cur = head.next
        while cur != None:
            tmptn = ListNode(val=cur.val)
            if cur.val < sorthead.val:
                tmptn.next = sorthead
                sorthead = tmptn
            else:
                sortcur = sorthead
                while sortcur.next != None:
                    if cur.val < sortcur.next.val:
                        tmptn.next = sortcur.next
                        sortcur.next = tmptn
                        break
                    sortcur = sortcur.next
                else:
                    sortcur.next = tmptn
            cur = cur.next
        return sorthead
        
