'''
https://leetcode.com/problems/hamming-distance/
'''
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum(int(x) for x in list(bin(x^y)[2:]))
        
