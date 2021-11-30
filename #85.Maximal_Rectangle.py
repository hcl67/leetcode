'''
https://leetcode.com/problems/maximal-rectangle/
'''
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if matrix == []:
            return 0
        m,n = len(matrix),len(matrix[0])
        hrd = [[0 for j in range(n)] for i in range(m)]
        vrd = [[defaultdict(int) for j in range(n)] for i in range(m)]
        ans = [[0 for j in range(n)] for i in range(m)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i > 0 and matrix[i-1][j] == '1':
                        hrd[i][j] = hrd[i-1][j] + 1
                    else:
                        hrd[i][j] = 1
                    if j > 0:
                        for k in range(1,hrd[i][j]+1):
                            vrd[i][j][k] = vrd[i][j-1][k]+k
                    else:
                        for k in range(1,hrd[i][j]+1):
                            vrd[i][j][k] = k
                    ans[i][j] = max(vrd[i][j].values())
        return max(ans[i][j] for i in range(m) for j in range(n))
                        
                    
        
