'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        dp = [[-999999] * 4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])
        print(dp)
        return max(dp[-1] + [0])
        '''
        b1,s1,b2,s2 = -999999,0,-999999,0
        for i in range(0,len(prices)):
            b1 = max(b1, -prices[i])
            s1 = max(s1, b1 + prices[i])
            b2 = max(b2, s1 - prices[i])
            s2 = max(s2, b2 + prices[i])
            #print(b1,s1,b2,s2)
        return max(b1,s1,b2,s2,0)
