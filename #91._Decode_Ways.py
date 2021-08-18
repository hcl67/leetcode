'''
https://leetcode.com/problems/decode-ways/
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        elif len(s) == 1:
            return 1
        c = [0]*len(s)
        c[0] = 1
        if s[1] == '0' and s[0] in {'1','2'}:
            c[1] = 1
        elif s[1] == '0':
            return 0
        elif s[0] == '1' or s[0] == '2' and s[1] in {'1','2','3','4','5','6'}:
            c[1] = 2
        else:
            c[1] = 1
        for j in range(2,len(s)):
            if s[j] == '0' and s[j-1] in {'1','2'}:
                c[j] = c[j-2]
            elif s[j] == '0':
                return 0
            elif s[j-1] == '1' or s[j-1] == '2' and s[j] in {'1','2','3','4','5','6'}:
                c[j] = c[j-2] + c[j-1]
            else:
                c[j] = c[j-1]
        return c[-1]
