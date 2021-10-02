'''
https://leetcode.com/problems/dungeon-game/
'''
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m,n = len(dungeon),len(dungeon[0])
        health = [[1] * n for _ in range(m)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if i == m-1 and j == n-1:
                    minout = 1
                else:
                    minout = math.inf
                    if i < m - 1:
                        minout = min(minout, health[i+1][j])
                    if j < n - 1:
                        minout = min(minout, health[i][j+1])
                health[i][j] = max(1, minout - dungeon[i][j])
        return health[0][0]
                
