'''
https://leetcode.com/problems/split-linked-list-in-parts/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        cur = head
        while cur != None:
            l += 1
            cur = cur.next
        d = l//k
        r = l%k
        ans = []
        j = 0
        cur = head
        while cur != None:
            if j == 0:
                ans += [cur]
            j += 1
            if r > 0 and j == d + 1 or r <= 0 and j == d:
                j = 0
                r -= 1
                tmp = cur.next
                cur.next = None
                cur = tmp
            else:
                cur = cur.next
        if k > l:
            for i in range(k-l):
                ans += [None]
        return ans
        
