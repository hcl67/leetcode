'''
https://leetcode.com/problems/flip-string-to-monotone-increasing/
'''
#看答案后可知，可以只扫一遍
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ln = len(s)
        s0 = [0] * ln
        s1 = [0] * ln
        if s[0] == '1':
            s0[0] = 1
        else:
            s0[0] = 0
        for i in range(1,ln):
            s0[i] = s0[i-1]
            if s[i] == '1':
                s0[i] += 1
        if s[ln-1] == '0':
            s1[ln-1] = 1
        else:
            s1[ln-1] = 0
        for i in range(ln-2,-1,-1):
            s1[i] = s1[i+1]
            if s[i] == '0':
                s1[i] += 1
        ss = [s1[0]] + [s0[i]+s1[i+1] for i in range(ln-1)] + [s0[ln-1]]
        return min(ss)
                
                
            
