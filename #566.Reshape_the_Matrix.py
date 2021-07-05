'''
https://leetcode.com/problems/reshape-the-matrix/
'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        if m*n != r*c:
            return mat
        flatmat = []
        for i in range(m):
            for j in range(n):
                flatmat.append(mat[i][j])
        newmat = [[0]*c for i in range(r)]
        for i in range(len(flatmat)):
            newmat[i//c][i%c] = flatmat[i]
        return newmat
        
