'''
https://leetcode.com/problems/minimum-height-trees/
'''
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        
        #无环图的最长链路的中间点
        #求最长链路，2次dfs
        if len(edges) == 0:
            return list(range(n))
        edgedict = defaultdict(set)
        for e in edges:
            edgedict[e[0]].add(e[1])
            edgedict[e[1]].add(e[0])
        edgedict = dict(edgedict)
        
        dq = deque([[0]])
        while dq:
            q = dq.popleft()
            ln = q[-1]
            for nn in edgedict[ln]:
                if nn not in q:
                    dq.append(q+[nn])
        dq = deque([[q[-1]]])
        while dq:
            q = dq.popleft()
            ln = q[-1]
            for nn in edgedict[ln]:
                if nn not in q:
                    dq.append(q+[nn])
        if len(q)%2 == 0:
            return q[len(q)//2-1:len(q)//2+1]
        else:
            return q[len(q)//2:len(q)//2+1]
        
        '''
        #Solution Trim Leaf思路
        while len(edgedict) > 2:
            trimnode = set(k for k,v in edgedict.items() if len(v) == 1)
            newedgedict = {k:v-trimnode for k,v in edgedict.items() if len(v)>1}
            edgedict = newedgedict
        return list(edgedict.keys())
        
        
        
        '''
        '''
        TLE

        @cache
        def _c(f,m):
            ans = {m}
            for n in edgedict[m] - {f}:
                ans |= _c(m,n) 
            return ans
        tree = [-1] * n
        tree[0] = 0
        l = 0
        while min(tree) < 0:
            nl = [i for i in range(n) if tree[i] == l]
            l += 1
            ns = set()
            for i in nl:
                ns |= edgedict[i]
            for j in ns:
                if tree[j] < 0:
                    tree[j] = l
        forest = [[] for _ in range(n)]
        forest[0] = tree
        unvisited = set(list(range(n))) - {0}
        flag = 1
        while flag:
            for tn in range(n):
                if forest[tn] == []:
                    continue
                potent = unvisited & {i for i in range(n) if forest[tn][i] == 1}
                #print(tn,potent)
                for pi in potent:
                    tree = [forest[tn][i] for i in range(n)]
                    rise = _c(tn,pi)
                    for i in range(n):
                        if i in rise:
                            tree[i] -= 1
                        else:
                            tree[i] += 1
                    forest[pi] = tree
                    unvisited -= {pi}
                if len(unvisited) == 0:
                    flag = 0
                    break
        mindept = min(max(i) for i in forest)
        return [i for i in range(n) if max(forest[i]) == mindept]
                    
                
        
        
        '''    
        
        '''
        TLE

        ans = []
        flag = 1
        tree = {}
        for i in range(n):
            tree[i] = {}
            tree[i][0] = set()
            tree[i][1] = {i}
        while flag:
            for i in range(n):
                step = tree[i][1]
                tree[i][0] |= tree[i][1]
                tree[i][1] = set()
                for j in step:
                    tree[i][1] |= edgedict[j]
                    tree[i][1] -= tree[i][0]
                if len(tree[i][0]) + len(tree[i][1]) == n:
                    flag = 0
                    ans.append(i)
        return ans
        '''        
        
        
        
        
        
        
