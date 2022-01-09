'''
https://leetcode.com/problems/robot-bounded-in-circle/
'''
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #一种是停留方向和初始方向不同，一种是回到(0,0)
        ds = [0] * 4
        d = 0
        for c in instructions:
            if c == 'G':
                ds[d] += 1
            elif c == 'L':
                d = (d-1)%4
            else:
                d = (d+1)%4
        return d != 0 or (ds[0] == ds[2] and ds[1] == ds[3])
        
