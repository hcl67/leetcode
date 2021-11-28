'''
https://leetcode.com/problems/all-paths-from-source-to-target/
'''
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        q = [[0]]
        ans = []
        while q:
            cur = q.pop()
            for j in graph[cur[-1]]:
                if j == len(graph)-1:
                    ans += [cur+[j]]
                else:
                    q += [cur+[j]]
        return ans
            
        
