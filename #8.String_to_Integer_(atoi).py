'''
https://leetcode.com/problems/string-to-integer-atoi/
'''
class Solution:
    def myAtoi(self, s: str) -> int:
        ans,sgn,lfg = 0,1,1
        for c in s:
            if lfg == 1 and c == ' ':
                continue
            elif lfg == 1 and c in "+-":
                if c == "-":
                    sgn = -1
                lfg = 0
            elif c in "0123456789":
                ans *= 10
                ans += int(c)
                lfg = 0
            else:
                break
        ans *= sgn
        if ans < -2**31:
            ans = -2**31
        elif ans > 2**31 - 1:
            ans = 2**31 - 1
        return ans
        
