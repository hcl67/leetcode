'''
https://leetcode.com/problems/erect-the-fence/
'''
class Solution:
    def outerTrees(self, trees: List[List[int]]) -> List[List[int]]:
        def geng(p1,p2):
            if p1[0] == p2[0]:
                if p1[1] <= p2[1]:
                    return math.inf
                else:
                    return -math.inf
            else:
                return (p2[1]-p1[1])/(p2[0]-p1[0])
        trees = [(t[0],t[1]) for t in trees]
        xmin = min(t[0] for t in trees)
        xmax = max(t[0] for t in trees)
        ymin = min(t[1] for t in trees)
        ymax = max(t[1] for t in trees)
        xminlst = [t for t in trees if t[0] == xmin]
        xmaxlst = [t for t in trees if t[0] == xmax]
        yminlst = [t for t in trees if t[1] == ymin]
        ymaxlst = [t for t in trees if t[1] == ymax]
        fence = set(xminlst+xmaxlst+yminlst+ymaxlst)
        lu = max(xminlst,key=lambda t:t[1])
        ul = min(ymaxlst,key=lambda t:t[0])
        ur = max(ymaxlst,key=lambda t:t[0])
        ru = max(xmaxlst,key=lambda t:t[1])
        ld = min(xminlst,key=lambda t:t[1])
        dl = min(yminlst,key=lambda t:t[0])
        dr = max(yminlst,key=lambda t:t[0])
        rd = min(xmaxlst,key=lambda t:t[1])
        f = [[lu],[ru],[ld],[rd]]
        fd = [[ul],[ur],[dl],[dr]]
        s = [1,-1,-1,1]
        g = [[math.inf],[math.inf],[math.inf],[math.inf]]
        tlst = [sorted([t for t in trees if t[0] <= ul[0] and t[0] > lu[0] and t[1] >= lu[1]])
               ,sorted([t for t in trees if t[0] >= ur[0] and t[0] < ru[0] and t[1] >= ru[1]], key = lambda x:(-x[0],x[1]))
               ,sorted([t for t in trees if t[0] <= dl[0] and t[0] > ld[0] and t[1] <= ld[1]], key = lambda x:(x[0], -x[1]))
               ,sorted([t for t in trees if t[0] >= dr[0] and t[0] < rd[0] and t[1] <= rd[1]], key = lambda x:(-x[0],-x[1]))]
        for i in range(4):
            if f[i]!=fd[i]:
                for t in tlst[i]:
                    if t[0] == f[i][-1][0]:
                        f[i] = f[i][:-1]
                        g[i] = g[i][:-1]
                    newg = geng(f[i][-1],t)*s[i]
                    while g[i][-1] < newg:
                        f[i] = f[i][:-1]
                        g[i] = g[i][:-1]
                        newg = geng(f[i][-1],t)*s[i]
                    if newg > 0:
                        f[i] += [t]
                        g[i] += [newg]                       
        fence.update(set(f[0]+f[1]+f[2]+f[3]))
        return list(fence)
                
        
        
        
