'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        #pass but not good enough 
        dp = [0,0,0]
        for i in range(3,len(prices)+2):
            dpi = dp[-1]
            for j in range(2,i):
                    dpi = max(dpi,dp[j-2]+prices[i-2]-prices[j-2])
            dp += [dpi]
        #print(dp)
        return dp[-1]
        '''
        #别人更好的解
        #dp[day][0] = max profit could have if we don't own stock at end of day and not in cooldown
        #dp[day][1] = max profit could have if we own stock at end of day
        #dp[day][2] = max profit could have if we sell the stock and are in cooldown at end of day
        
        # 转移关系 0->0/1 1->1/2 2->0
        
        dp = [[0 for _ in range(3)] for _ in range(len(prices))]
        dp[0][1] -= prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][2])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
            dp[i][2] = dp[i-1][1] + prices[i]

        return max(dp[-1])   
