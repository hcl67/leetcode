'''
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
'''
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        import bisect
        n = len(matrix)
        vallist = [matrix[0][0]]
        indset = {(0,0)}
        valinddict = {matrix[0][0]:{(0,0)}}
        totcnt = 0
        while(1):
            popval = vallist[0]
            popindset = valinddict[popval]
            popvalcnt = len(popindset)
            if totcnt + popvalcnt >= k:
                return popval
            else:
                totcnt += popvalcnt
            del valinddict[popval]
            vallist[:popvalcnt] = []
            for ind in popindset:
                i = ind[0]
                j = ind[1]
                if i < n-1 and (i+1,j) not in indset:
                    newval = matrix[i+1][j]
                    pos = bisect.bisect_left(vallist,newval)
                    vallist.insert(pos,newval)
                    indset.add((i+1,j))
                    if newval in valinddict:
                        valinddict[newval].add((i+1,j))
                    else:
                        valinddict[newval] = {(i+1,j)}
                if j < n-1 and (i,j+1) not in indset:
                    newval = matrix[i][j+1]
                    pos = bisect.bisect_left(vallist,newval)
                    vallist.insert(pos,newval)
                    indset.add((i,j+1))
                    if newval in valinddict:
                        valinddict[newval].add((i,j+1))
                    else:
                        valinddict[newval] = {(i,j+1)}                
            indset -= popindset
            
