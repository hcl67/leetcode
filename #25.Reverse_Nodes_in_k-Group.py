'''
https://leetcode.com/problems/reverse-nodes-in-k-group/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head.next == None or k == 1:
            return head
        ans = pre = ListNode(next=head)
        cur = head        
        ind = 0
        while(cur != None):
            ind += 1
            if ind%k == 1:  #翻转链的头
                shtlisttl = ListNode(val = cur.val)
                shtlisthd = shtlisttl
            else:
                shtlisthd = ListNode(val = cur.val, next = shtlisthd)
                if ind%k == 0:  #翻转链的尾
                    pre.next = shtlisthd
                    shtlisttl.next = cur.next
                    pre = shtlisttl
            cur = cur.next
        return ans.next
