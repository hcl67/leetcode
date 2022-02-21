'''
https://leetcode.com/problems/the-skyline-problem/
'''
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        from sortedcontainers import SortedList
        q = {0:inf}
        ans = []
        lvl = SortedList([0])
        for cbd in buildings:
            while cbd[0] > q[lvl[-1]]:
                pr = q.pop(lvl.pop())
                while pr > q[lvl[-1]]:
                    q.pop(lvl.pop())
                else:
                    if pr == ans[-1][0]:
                        ans[-1][1] = min(lvl[-1],ans[-1][0])
                    else:
                        ans.append([pr,lvl[-1]])
            if cbd[2] > lvl[-1]:
                if ans and cbd[0] == ans[-1][0]:
                    ans[-1][1] = max(cbd[2],ans[-1][0])
                else:
                    ans.append([cbd[0],cbd[2]])
            if cbd[2] in q:
                q[cbd[2]] = max(q[cbd[2]],cbd[1])
            else:
                lvl.add(cbd[2])
                q[cbd[2]] = cbd[1]
        while len(lvl) > 1:
            pr = q.pop(lvl.pop())
            while pr > q[lvl[-1]]:
                q.pop(lvl.pop())
            else:        
                if pr == ans[-1][0]:
                    ans[-1][1] = min(lvl[-1],ans[-1][0])
                else:
                    ans.append([pr,lvl[-1]])         
        return ans
        
