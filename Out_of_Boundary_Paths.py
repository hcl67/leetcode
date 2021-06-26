'''
https://leetcode.com/problems/out-of-boundary-paths/
'''
class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        import copy
        grid0 = [[0 if 1<=j<=n and 1<=i<=m else 1 for j in range(n+2)] for i in range(m+2)]
#        print("grid0:", grid0)
        for move in range(maxMove):
            grid1 = [[(grid0[i-1][j] + grid0[i+1][j] + grid0[i][j-1] + grid0[i][j+1]) % (10**9 + 7) if 1<=j<=n and 1<=i<=m else 1 for j in range(n+2)] for i in range(m+2)]
#            print("grid1:", grid1)
            grid0 = copy.deepcopy(grid1)
        return grid0[startRow+1][startColumn+1]

      
'''
构造 f(m,i,j) 1<=m<=maxMove, 1<=i<=m, 1<=j<=n,表示恰好m步移出边界的方法数，那么
f(m,i,j) = f(m-1,i+/-1,j+/-1)
边界条件 m = 1是 四角为2 四边为1 注意i,j退化的场景
return= sum(f(m, startRow, startColumn), m = 1~maxMove)
加一圈边界为0

进化：
加一圈边界条件为1
f(m,i,j) = f(m-1,i+/-1,j+/-1), 如此构造出的f(m,i,j)即表示m步时总共的方法，理解方式：边界外的1表示边界上的点在此轮可以增加的1步移出的新方式，加上边界内的多一步的老方式，无重复

'''        
