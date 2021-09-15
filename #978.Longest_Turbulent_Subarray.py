'''
https://leetcode.com/problems/longest-turbulent-subarray/
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def sign(a):
            return (a > 0) - (a < 0)
        
        if len(arr) == 1:
            return 1
        ans,cur,sgn = 1,1,0
        for i in range(1,len(arr)):
            newsgn = sign(arr[i]-arr[i-1])
            if newsgn == 0:
                cur = 1
            elif sgn*newsgn == -1:
                cur += 1
            else:
                cur = 2
            sgn = newsgn
            ans = max(ans,cur)
        return ans
            
            
        
