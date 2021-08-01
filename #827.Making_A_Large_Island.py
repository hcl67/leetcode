'''
https://leetcode.com/problems/making-a-large-island/
'''
class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if n == 1:
            return 1
# 通过并查集获得每个岛的大小
        
        def getdsu(p,dsu):
            if dsu[p[0]][p[1]] != (p[0],p[1]):
                dsu[p[0]][p[1]] = getdsu(dsu[p[0]][p[1]],dsu)
            return dsu[p[0]][p[1]]
        
        def undsu(p1,p2,dsu,size):
            p1 = getdsu(p1,dsu)
            p2 = getdsu(p2,dsu)
            if p1 == p2:
                return
            elif size[p1] >= size[p2]:
                dsu[p2[0]][p2[1]] = p1
                size[p1] += size[p2]
                del size[p2]
            else:
                dsu[p1[0]][p1[1]] = p2
                size[p2] += size[p1]
                del size[p1]
            return
        
        dsu = [[(i,j) for j in range(n)] for i in range(n)]
        size = {(i,j):1 if grid[i][j]==1 else 0 for j in range(n) for i in range(n)}        
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni,nj = i+di,j+dj
                        if ni>=0 and ni<n and nj>=0 and nj<n and grid[ni][nj] == 1:
                            undsu((i,j),(ni,nj),dsu,size)
                    
#        print(size)

# 遍历所有0，找出0四方最大的2个岛和0连起来，找出最大的岛        
        ans = max(size.values())
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    sl = []
                    pl = []
                    for di,dj in [(-1,0),(1,0),(0,-1),(0,1)]:
                        ni,nj = i+di,j+dj
                        if ni>=0 and ni<n and nj>=0 and nj<n and grid[ni][nj] == 1:
                            p = getdsu((ni,nj),dsu)
                            if p not in pl:
                                sl.append(size[p])
                                pl.append(p)    

                    ans = max(ans, 1+sum(sl))
                                  
        return ans
                                  
            
                       
                
