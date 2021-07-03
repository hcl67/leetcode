'''
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/
'''

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:


        m = len(matrix)
        n = len(matrix[0])

        t1l = []
        for i in range(m):
            li = []
            for j1 in range(n):
                s = 0
                for j2 in range(j1,n):
                    s+= matrix[i][j2]
                    li += [s]
            t1l += [li]
        ans = []
        for j in range(n*(n+1)//2):
            cursum = t1l[0][j]
            if cursum <= k:
                bestsum = cursum
            else:
                bestsum = -9999999999999
            if cursum > 0:
                li = [0, cursum]
            else:
                li = [cursum, 0]
            for i in range(1,m):
                cursum += t1l[i][j]
                it = bisect.bisect_left(li, cursum-k)
                if it!=len(li):
                    bestsum = max(bestsum, cursum-li[it])
                li.insert(bisect.bisect_left(li, cursum), cursum)
            ans += [bestsum]                

        return max(ans)
