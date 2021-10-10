'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bl,br = bin(left)[2:],bin(right)[2:]
        if len(bl) != len(br):
            return 0
        ans = ''
        i = 0
        while i < len(br) and bl[i] == br[i]:
            i += 1
        ans += br[:i] + '0'*(len(br)-i)
        return int(ans,2)
