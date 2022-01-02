'''
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
'''
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        d = [0]*60
        for t in time:
            d[t%60] += 1
        ans = sum(d[i]*d[60-i] for i in range(1,30))
        ans += d[0]*(d[0]-1)//2 + d[30]*(d[30]-1)//2
        return ans
