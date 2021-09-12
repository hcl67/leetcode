'''
https://leetcode.com/problems/reachable-nodes-in-subdivided-graph/
'''
class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        ed = defaultdict(list)
        for e in edges:
            ed[e[0]] += [[e[1],e[2]]]
            ed[e[1]] += [[e[0],e[2]]]
        nq = defaultdict(int)
        for e0 in ed[0]:
            if maxMoves-e0[1]>0:
                nq[e0[0]] = maxMoves-e0[1]-1
        nl = {0:maxMoves}
        while len(nq) > 0:
            node = max(nq.keys(),key = lambda x:nq[x])
            mm = nq[node]
            del nq[node]
            nl[node] = mm
            for e0 in ed[node]:
                if mm-e0[1]>0 and e0[0] not in nl:
                    nq[e0[0]] = max(nq[e0[0]],mm-e0[1]-1)
        ans = 0
        for k,v in nl.items():
            for e in ed[k]:
                if e[0] in nl:
                    ans += min(e[1],v+nl[e[0]])/2
                else:
                    ans += v                
        return int(ans)+len(nl)
