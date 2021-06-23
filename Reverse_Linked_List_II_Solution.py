# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:

        prehd = ListNode(val = -999)
        pretl = ListNode()
        revhd = ListNode()
        revtl = ListNode()
        psthd = ListNode(val = -999)


        ind = 1
        voidhead = ListNode(val = -999, next = head)
        curpt  = head
        lstpt = voidhead
        
        while(curpt != None):
            nxtpt = curpt.next
            if ind < left:
                if ind == 1:
                    prehd = curpt
                if ind == left - 1:
                    pretl = curpt
            if ind == left:
                revtl = curpt
            if ind == right:
                revhd = curpt
            if ind > left and ind <= right:
                curpt.next = lstpt                
            if ind == right + 1:
                psthd = curpt
            
            lstpt = curpt
            curpt = nxtpt
            ind += 1
            
        if psthd.val > -999:
            revtl.next = psthd
        else:
            revtl.next = None
        if prehd.val > -999:
            pretl.next = revhd
            return prehd
        else:
            return revhd
        
