'''
https://leetcode.com/problems/climbing-stairs/submissions/
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def _f(n):
            if n <= 1:
                return 1
            else:
                return _f(n-1) + _f(n-2)
        return _f(n)
        
