'''
https://leetcode.com/problems/sum-of-distances-in-tree/
'''
        def dfs1(u,f):
            sz[u] = 1
            dp[u] = 0
            for v in graph[u]:
                if v==f:
                    continue
                dfs1(v,u)
                dp[u] += (dp[v] + sz[v])
                sz[u] += sz[v]
        
        def dfs2(u,f):
            ans[u] = dp[u]
            for v in graph[u]:
                if v == f:
                    continue   
                pu = dp[u]
                pv = dp[v]
                su = sz[u]
                sv = sz[v]
                dp[u] -= (dp[v]+sz[v])
                sz[u] -= sz[v]
                dp[v] += (dp[u]+sz[u])
                sz[v] += sz[u]
                dfs2(v,u)
                dp[u] = pu
                dp[v] = pv
                sz[u] = su
                sz[v] = sv
        ans = [0 for i in range(n)]
        sz = [0 for i in range(n)]
        dp = [0 for i in range(n)]
        graph = [[]for i in range(n)]
        for edge in edges:
            u = edge[0]
            v = edge[1]
            graph[u].append(v)
            graph[v].append(u)
        dfs1(0,-1)
        dfs2(0,-1)
        return ans
#trial 2 还是太慢
    if len(edges)==0:
    return [0]
    fd = {}
    for e in edges:
        e0,e1 = e
        if e0 in fd and e1 not in fd:
            fd[e1] = {}
            for k in list(fd[e0].keys()):
                fd[e1][k] = fd[k][e1] = fd[k][e0] + 1
            fd[e0][e1] = fd[e1][e0] = 1
            
        elif e1 in fd and e0 not in fd:
            fd[e0] = {}
            for k in list(fd[e1].keys()):
                fd[e0][k] = fd[k][e0] = fd[k][e1] + 1
            fd[e1][e0] = fd[e0][e1] = 1
                
        elif e1 in fd and e0 in fd:
            l0 = list(fd[e0].keys())
            l1 = list(fd[e1].keys())
            for k0 in l0:
                for k1 in l1:
                    fd[k0][k1] = fd[k1][k0] = fd[e0][k0] + 1 + fd[e1][k1]
                    fd[e0][k1] = fd[k1][e0] = 1 + fd[e1][k1]
                fd[e1][k0] = fd[k0][e1] = 1 + fd[e0][k0]
            fd[e0][e1] = fd[e1][e0] = 1 
        
        else:
            fd[e0] = {}
            fd[e1] = {}
            fd[e0][e1] = fd[e1][e0] = 1 
            
    return [sum(fd[i].values()) for i in range(n)]  
    


#trial 1 太慢
    if len(edges)==0:
        return [0]
    elif len(edges)==1:
        return [1,1]
    else:
        fd = {}
        od = {}
        for e in edges:
            fd[(e[0],e[1])] = fd[(e[1],e[0])] = 1
            od[(e[0],e[1])] = od[(e[1],e[0])] = 1
        while len(fd) < n*(n-1):
            ud = {}
            for e1 in fd.keys():
                for e2 in od.keys():
                    if e1[1] != e2[0] or e1[0] == e2[1] or (e1[0],e2[1]) in fd:
                        continue
                    ud[(e1[0],e2[1])] = ud[(e2[1],e1[0])] = fd[e1]+od[e2]
            fd.update(ud)
        #print(fd)
        ans = [0]*n
        for i in range(n):
            for j in range(n):
                if j==i:
                    continue
                else:
                    ans[i] += fd[(i,j)]
        return ans
'''                                
