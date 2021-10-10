'''
https://leetcode.com/problems/bitwise-and-of-numbers-range/
'''
class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bl,br = bin(left)[2:],bin(right)[2:]
        if len(bl) != len(br):
            return 0
        ans = ''
        for i in range(len(bl)):
            if bl[i] == br[i]:
                ans += bl[i]
            else:
                break
        ans += '0'*(len(br)-len(ans))
        return int(ans,2)
        
