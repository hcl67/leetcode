'''
https://leetcode.com/problems/linked-list-cycle-ii/
'''
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        lst = set()
        while cur:
            lst.add(cur)
            cur = cur.next
            if cur in lst:
                return cur
        return None
        
