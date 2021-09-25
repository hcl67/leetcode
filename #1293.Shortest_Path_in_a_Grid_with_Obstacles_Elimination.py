'''
https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/
'''
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        
        m, n = len(grid), len(grid[0])
        Q, v = deque([(0, 0, 0, k)]), set()
        
        if k >= m + n - 2: return m + n - 2
        
        while Q:
            steps, x, y, k = Q.popleft()
            if (x, y) == (n-1, m-1): return steps
            
            for dx, dy in (x, y-1), (x, y+1), (x-1, y), (x+1, y):
                if 0 <= dx < n and 0 <= dy < m and k - grid[dy][dx] >= 0:
                    new = (dx, dy, k - grid[dy][dx])
                    if new not in v:
                        v.add(new)
                        Q.append((steps + 1,) + new)
            
        return -1        
        
        '''
        m,n = len(grid),len(grid[0])
        path = [[{} for j in range(n)] for i in range(m)]
        def _upd(i,j,updp):
            updf = 0
            curp = path[i][j]
            if grid[i][j] == 0:
                for _k,_v in updp.items():
                    if _k in curp and curp[_k] <= _v + 1:
                        continue
                    else:
                        curp[_k] = _v + 1
                        updf = 1
            else:
                for _k,_v in updp.items():
                    if _k >= k or _k+1 in curp and curp[_k+1] <= _v + 1:
                        continue
                    else:
                        curp[_k+1] = _v + 1
                        updf = 1
            if updf == 1:
                if i > 0:
                    _upd(i-1,j,curp)
                if i < m-1:
                    _upd(i+1,j,curp)
                if j > 0:
                    _upd(i,j-1,curp)
                if j < n-1:
                    _upd(i,j+1,curp)
        _upd(0,0,{0:-1})
        if len(path[m-1][n-1]) == 0:
            return -1
        else:
            return min(path[m-1][n-1].values())          
                
        '''
