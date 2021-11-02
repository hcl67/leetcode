'''
https://leetcode.com/problems/unique-paths-iii/
'''
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        pathlen = 2
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    st = (i,j)
                elif grid[i][j] == 2:
                    ed = (i,j)
                elif grid[i][j] == 0:
                    pathlen += 1
        ans = []
        pathque = deque()
        pathque.append([st])
        while pathque:
            curpath = pathque.popleft()
            curcell = curpath[-1]
            #print(curpath,curcell)
            if len(curpath) == pathlen and curcell == ed:
                ans += [curpath]
                continue
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                nxtcell = (curcell[0]+d[0],curcell[1]+d[1])
                if 0 <= nxtcell[0] < len(grid) and 0 <= nxtcell[1] < len(grid[0]):
                    if grid[nxtcell[0]][nxtcell[1]] != -1 and nxtcell not in curpath:
                        pathque.append(curpath+[nxtcell])
        return len(ans)
        
