'''
https://leetcode.com/problems/maximal-square/
'''
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m,n = len(matrix),len(matrix[0])
        ans = [[0 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i==0 or j==0:
                        ans[i][j] = 1
                    else:
                        ans[i][j] = min(ans[i-1][j-1],ans[i-1][j],ans[i][j-1])+1
        return max([max(l) for l in ans])**2
                    
