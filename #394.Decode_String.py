'''
https://leetcode.com/problems/decode-string/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        def _c(n,s):
            ps = ''
            k = 0
            bflag = 0
            for i in range(len(s)):
                if bflag == 0 and s[i] in string.digits:
                    k = k*10 + int(s[i])
                elif bflag == 0 and s[i] == '[':
                    ts = ''
                    bflag += 1
                elif bflag > 0 and s[i] == '[':
                    bflag += 1
                    ts += s[i]
                elif bflag > 1 and s[i] == ']':
                    bflag -= 1
                    ts += s[i]
                elif bflag == 1 and s[i] == ']':
                    bflag -= 1
                    ps += _c(k,ts)
                    k = 0
                elif bflag > 0:
                    ts += s[i]
                else:
                    ps += s[i]
            return ps*n
        return _c(1,s)
        
