'''
https://leetcode.com/problems/swim-in-rising-water/
'''
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        N = len(grid)
        def getadjland(tup):
            tupadj = [(tup[0]+1,tup[1]),(tup[0],tup[1]+1),(tup[0]-1,tup[1]),(tup[0],tup[1]-1)]
            tupadj2 = [t for t in tupadj if t[0]>=0 and t[0]<N and t[1]>=0 and t[1]<N]
            return tupadj2
        
        landed = {}  #记录之前已经可以达到的grid
        newland = {(0,0):grid[0][0]}  #记录最新一轮可以到达的grid
        adjland = {}  #记录下一轮可以到达的未到达过的grid
        t = grid[0][0]  
        while(1):
            #step1: 寻找newland中未到达过的grid
            for i_newl in newland.keys():
                newadj = getadjland(i_newl)
                for i_newadj in newadj:
                    if i_newadj not in list(adjland.keys()) + list(newland.keys()) + list(landed.keys()):
                        adjland[i_newadj] = grid[i_newadj[0]][i_newadj[1]]
#            print("step1:adjland:", adjland)
            
            #step2: 将newland搬到landed
            landed.update(newland)
            newland = {}
#            print("step2:landed:", landed)
            if (N-1,N-1) in landed.keys():
                break
            
            #step3: 寻找新的newland，如果水位不够，提高水位
            t = max(min(adjland.values()), t)
            for i_k, i_v in list(adjland.items()):
                if i_v <= t:
                    newland[i_k] = i_v
                    del adjland[i_k]
#            print("step3:t:",t)
#            print("step3:newland:",newland)
#            print("step3:adjland:",adjland)
                    
        return t
            
        
