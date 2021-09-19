'''
https://leetcode.com/problems/distinct-subsequences/
'''
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache
        def _g(s,t):
            if len(s) == 0 or len(s)<len(t):
                return 0
            elif len(t) == 0 or s == t:
                return 1
            elif len(s) == len(t):
                return 0
            elif s[0] == t[0]:
                return _g(s[1:],t[1:]) + _g(s[1:],t)
            else:
                return _g(s[1:],t)
        return _g(s,t)
        
