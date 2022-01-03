'''
https://leetcode.com/problems/find-the-town-judge/
'''
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        '''
        if n == 1 and len(trust) == 0:
            return 1
        t0,t1 = defaultdict(set),defaultdict(set)
        for tr in trust:
            t0[tr[0]].add(tr[1])
            t1[tr[1]].add(tr[0])
        ans = [i for i in [k for k in t1.keys() if len(t1[k])==n-1] if len(t0[i]) == 0]
        if len(ans) == 1:
            return ans[0]
        else:
            return -1
        '''
        
        count = [0] * (n+1)
        for i,j in trust:
            count[i] -= 1
            count[j] += 1
        for i in range(1,n+1):
            if count[i] == n-1:
                return i
        return -1
        
        
