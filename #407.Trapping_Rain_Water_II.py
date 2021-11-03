'''
https://leetcode-cn.com/problems/trapping-rain-water-ii/
'''
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:

    # h[i][j] = max(heightMap[i][j],min(h[i-1][j],h[i][j-1],h[i+1][j],h[i][j+1]))

        m,n = len(heightMap),len(heightMap[0])
        h = [[heightMap[i][j] for j in range(n)] for i in range(m)]
        for i in range(1,m-1):
            for j in range(1,n-1):
                h[i][j] = 20000        

        #print(h)      
        def _c(i,j,val):
            if h[i][j] > max(val,heightMap[i][j]):
                h[i][j] = max(val,heightMap[i][j])
                if i > 1 and h[i][j] < h[i-1][j]:
                    _c(i-1,j,h[i][j])
                if i < m-1 and h[i][j] < h[i+1][j]:
                    _c(i+1,j,h[i][j])
                if j > 1 and h[i][j] < h[i][j-1]:
                    _c(i,j-1,h[i][j])
                if j < n-1 and h[i][j] < h[i][j+1]:
                    _c(i,j+1,h[i][j])
        for i in range(1,m-1):
            for j in range(1,n-1):
                _c(i,j,min(h[i-1][j],h[i][j-1],h[i+1][j],h[i][j+1]))
          
        return sum(h[i][j]-heightMap[i][j] for i in range(1,m-1) for j in range(1,n-1))
