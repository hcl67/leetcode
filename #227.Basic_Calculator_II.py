'''
https://leetcode.com/problems/basic-calculator-ii/
'''
#using stack would be better
class Solution:
    def calculate(self, s: str) -> int:
        ans = []
        d = ""
        for c in s:
                if c == " ":
                    continue
                elif c in string.digits:
                    d += c
                elif c in {'+','-','*','/'}:
                    if d:
                        ans += [int(d)]
                        d = ""
                    ans += [c]
        else:
            if d:
                ans += [int(d)]               
        i = 0
        while i < len(ans):
            if ans[i] == "*":
                ans = ans[:i-1] + [ans[i-1]*ans[i+1]] + ans[i+2:]
            elif ans[i] == "/":
                ans = ans[:i-1] + [ans[i-1]//ans[i+1]] + ans[i+2:]
            else:
                i += 1
        if ans[0] in {'+','-'}:
            r = 0
            i = 0
        else:
            r = ans[0]
            i = 1
        while i < len(ans):
            if ans[i] == "+":
                r += ans[i+1]
                i += 2
            elif ans[i] == "-":
                r -= ans[i+1]
                i += 2
        return r
        
