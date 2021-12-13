'''
https://leetcode.com/problems/consecutive-characters/
'''
class Solution:
    def maxPower(self, s: str) -> int:
        ans,cln,chr = 1,1,s[0]
        for c in s[1:]:
            if c == chr:
                cln += 1
                ans = max(ans,cln)
            else:
                cln,chr = 1,c
        return ans
        
