'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b,s = -999999,0
        for i in range(0,len(prices)):
            b = max(b, s - prices[i])
            s = max(s, b + prices[i])
            #print(b1,s1,b2,s2)
        return s
