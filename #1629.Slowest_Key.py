'''
https://leetcode.com/problems/slowest-key/
'''
class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        releaseTimes = [0]+releaseTimes
        l = [(releaseTimes[i+1]-releaseTimes[i],keysPressed[i]) for i in range(len(keysPressed))]
        return sorted(l,reverse=True)[0][1]
