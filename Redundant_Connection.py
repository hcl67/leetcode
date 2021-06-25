class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        #广度优先遍历
        lcs = [[1]] #loop candidates
        flagloop = 1
        loop = []
        while(1):
            newlcs = []
            for lc in lcs:
                for ed in edges:
                    #关联上新的点
#                    print("lc:", lc)
#                    print("ed:", ed)
                    if ed[0] == lc[-1] and (len(lc) == 1 or len(lc) > 1 and ed[1] != lc[-2]):
                        newlc = lc + [ed[1]]
                    elif ed[1] == lc[-1] and (len(lc) == 1 or len(lc) > 1 and ed[0] != lc[-2]):
                        newlc = lc + [ed[0]]
                    else:
                        continue
                    #判断是否形成环
#                    print("newlc:", newlc)
                    if newlc[-1] in newlc[:-1]:
#                        print("newlc with loop:", newlc)
                        flagloop = 0
                        loop = newlc[newlc[:-1].index(newlc[-1]):]
#                        print("loop:", loop)
                        break
                    newlcs.append(newlc)
                if flagloop == 0:
                    break
            if flagloop == 0:
                break
            else:
                lcs = [tt for tt in newlcs]
#                print("lcs:", lcs)
        
        #寻找环中最后一条边
        loopedge = []
        for s in range(1, len(loop)):
            ed0 = [loop[s-1], loop[s]]
            ed1 = [loop[s], loop[s-1]]
            if ed0 in edges:
                loopedge.append(edges.index(ed0))
            else:
                loopedge.append(edges.index(ed1))
            
        maxedge = edges[max(loopedge)]
#        print(maxedge)
        return maxedge
            
                
                    
                    
                    
'''
逻辑判断，树加一条边只会形成一个环

'''                    
                        
