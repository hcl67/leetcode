'''
https://leetcode.com/problems/smallest-integer-divisible-by-k/
'''
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1:
            return 1
        if k%2 == 0 or k%5 == 0:
            return -1
        r = 1
        n = 1
        while 1:
            n += 1
            r = (r * 10 + 1) % k
            if r == 1:
                return -1
            if r == 0:
                return n
        
            
            
