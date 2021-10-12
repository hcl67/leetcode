'''
https://leetcode.com/problems/guess-number-higher-or-lower/
'''
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        maxp,minp = n+1,0
        while 1:
            g = (maxp+minp)//2
            r = guess(g)
            if r == 0:
                return g
            elif r == -1:
                maxp = min(g,maxp-1)
            else:
                minp = max(g,minp+1)
            
        
