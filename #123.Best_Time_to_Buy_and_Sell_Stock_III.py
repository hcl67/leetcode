'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 0 第一次买入股票
        # 1 第一次卖出股票
        # 2 第二次买入股票
        # 3 第二次卖出股票
        dp = [[-999999] * 4 for _ in range(len(prices))]
        dp[0][0] = -prices[0]
        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0], -prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] + prices[i])
            dp[i][2] = max(dp[i-1][2], dp[i-1][1] - prices[i])
            dp[i][3] = max(dp[i-1][3], dp[i-1][2] + prices[i])
        print(dp)
        return max(dp[-1] + [0])
        
