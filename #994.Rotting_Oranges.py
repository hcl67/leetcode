'''
https://leetcode.com/problems/rotting-oranges/
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fsh,rot = set(),set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fsh.add((i,j))
                elif grid[i][j] == 2:
                    rot.add((i,j))
        ans = 0
        while 1:
            newrot = set()
            for o in fsh:
                for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                    if (o[0]+d[0],o[1]+d[1]) in rot:
                        newrot.add(o)
                        break
            if len(newrot) == 0:
                break
            ans += 1
            rot |= newrot
            fsh -= newrot
        if len(fsh) > 0:
            return -1
        else:
            return ans
        
