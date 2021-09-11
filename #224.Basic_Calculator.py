'''
https://leetcode.com/problems/basic-calculator/
'''
class Solution:
    def calculate(self, s: str) -> int:
        ans = [0]
        sg = [1]
        j = 0
        d = 0
        i = 0
        while i < len(s):
            c = s[i]
            if c == '+':
                ans[j] += sg[j] * d
                sg[j],d = 1,0
            elif c == '-':
                ans[j] += sg[j] * d
                sg[j],d = -1,0
            elif c in {'0','1','2','3','4','5','6','7','8','9'}:
                d *= 10
                d += int(c)
            elif c == '(':
                j += 1
                ans += [0]
                sg += [1]
            elif c == ')':
                ans[j] += sg[j] * d
                j -= 1
                ans[j] += ans[j+1]*sg[j]
                ans = ans[:-1]
                sg = sg[:-1]
                d = 0
            i += 1    
        ans[j] += sg[j]*d
        return ans[0]
