'''
https://leetcode.com/problems/cherry-pickup-ii/
'''
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        m,n = len(grid),len(grid[0])
        q = {}
        r = 0
        q[(0,n-1)] = grid[0][0]+grid[0][n-1]
        while r < m-1:
            r += 1
            nq = defaultdict(int)
            for c,cnt in q.items():
                c1,c2 = c
                for d1 in (-1,0,1):
                    for d2 in (-1,0,1):
                        nc1,nc2 = c1+d1,c2+d2
                        if nc1 < 0 or nc2 >= n or nc2 < nc1:
                            continue
                        if nc1 == nc2:
                            ncnt = cnt + grid[r][nc1]
                        else:
                            ncnt = cnt + grid[r][nc1] + grid[r][nc2]
                        nq[(nc1,nc2)] = max(ncnt,nq[(nc1,nc2)])
            q = dict(nq)
            #print(q)
        return max(q.values())
                    
        
