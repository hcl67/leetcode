'''
https://leetcode.com/problems/gas-station/
'''
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        net = [gas[i]-cost[i] for i in range(len(gas))]
        s,i,t = 0,0,0
        while 1:
            t += net[i]
            i += 1
            i %= len(gas)
            if i == s:
                return s
            if t < 0:
                s,t = i,0
            
                
                
