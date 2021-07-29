'''
https://leetcode.com/problems/01-matrix/
'''
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
 # DP 参考答案后
        m = len(mat)
        n = len(mat[0])
        dismat = [[99999999 for j in range(n)] for i in range(m)] 
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dismat[i][j] = 0
                else:
                    if i>0:
                        dismat[i][j] = min(dismat[i][j],dismat[i-1][j]+1)
                    if j>0:
                        dismat[i][j] = min(dismat[i][j],dismat[i][j-1]+1)
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if mat[i][j] == 0:
                    dismat[i][j] = 0
                else:
                    if i<m-1:
                        dismat[i][j] = min(dismat[i][j],dismat[i+1][j]+1)
                    if j<n-1:
                        dismat[i][j] = min(dismat[i][j],dismat[i][j+1]+1)
                
        return dismat
        
'''
一个比较差的BFS
        
        
        m = len(mat)
        n = len(mat[0])
        dismat = [[-1 for j in range(n)] for i in range(m)] 
        tot = 0
        lvl = 0
        while tot < m*n:
            for i in range(m):
                for j in range(n):
                    if dismat[i][j] >= 0:
                        continue
                    elif mat[i][j] == 0:
                        dismat[i][j] = 0
                        tot += 1
                    else:
                        adj = [(i+x,j) for x in [-1,1] if i+x>=0 and i+x<m]
                        adj += [(i,j+y) for y in [-1,1] if j+y>=0 and j+y<n]
                        adjdis = list(filter(lambda x:x>=0,[dismat[x[0]][x[1]] for x in adj]))
                        if len(adjdis) > 0 and min(adjdis) < lvl:
                            dismat[i][j] = min(adjdis)+1
                            tot += 1
            lvl += 1
        return dismat
                                   
'''        
