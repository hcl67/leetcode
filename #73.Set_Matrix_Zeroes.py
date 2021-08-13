'''
https://leetcode.com/problems/set-matrix-zeroes/
'''
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        rset = set()
        cset = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rset.add(i)
                    cset.add(j)
        for i in range(n):
            for j in range(m):
                if i in rset or j in cset:
                    matrix[i][j] = 0
        return
                    
                
        
