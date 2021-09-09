'''
https://leetcode.com/problems/largest-plus-sign/
'''
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        ma = [[[1,1] for j in range(n)] for i in range(n)]
        for x in mines:
            ma[x[0]][x[1]] = [0,0]
        for i in range(1,n-1):
            for j in range(1,n-1):
                ma[i][j][0] *= ma[i-1][j][0]+1
                ma[i][j][1] *= ma[i][j-1][1]+1
        for i in range(n-2,0,-1):
            for j in range(n-2,0,-1):
                ma[i][j][0] = min(ma[i+1][j][0]+1,ma[i][j][0])
                ma[i][j][1] = min(ma[i][j+1][1]+1,ma[i][j][1])
        return max(max(min(ma[i][j]) for j in range(n)) for i in range(n))
            
            
        
