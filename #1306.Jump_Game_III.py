'''
https://leetcode.com/problems/jump-game-iii/
'''
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        if arr[start] == 0:
            return True
        dq = deque([start])
        visited = {start}
        while dq:
            cur = dq.pop()
            nxt = [cur+arr[cur],cur-arr[cur]]
            for n in nxt:
                if n >= 0 and n < len(arr) and n not in visited:
                    if arr[n] == 0:
                        return True
                    visited.add(n)
                    dq.append(n)
        return False
