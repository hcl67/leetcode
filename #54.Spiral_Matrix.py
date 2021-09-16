'''
https://leetcode.com/problems/spiral-matrix/
'''
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        i0,i1 = 0,len(matrix)
        j0,j1 = 0,len(matrix[0])
        m,n = i1,j1
        d = 0
        ans = []
        while len(ans)< m * n:
            if d == 0:
                ans += [matrix[i0][j] for j in range(j0,j1)]
                i0 += 1
                d = 1
            elif d == 1:
                ans += [matrix[i][j1-1] for i in range(i0,i1)]
                j1 -= 1
                d = 2
            elif d == 2:
                ans += [matrix[i1-1][j] for j in range(j1-1,j0-1,-1)]
                i1 -= 1
                d = 3
            elif d == 3:
                ans += [matrix[i][j0] for i in range(i1-1,i0-1,-1)]
                j0 += 1
                d = 0
        return ans
      
