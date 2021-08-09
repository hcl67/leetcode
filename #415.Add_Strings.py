'''
https://leetcode.com/problems/add-strings/
'''
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        if num1== '0':
            return num2
        if num2 == '0':
            return num1
        if len(num2) > len(num1):
            num1,num2 = num2,num1
        n1,n2 = len(num1),len(num2)
        mf = 0
        ans = ''
        for k in range(-1,-n1-1,-1):
            d1 = int(num1[k])
            if k >= -n2:
                d2 = int(num2[k])
            else:
                d2 = 0
            d = d1+d2+mf
            if d>=10:
                mf = 1
            else:
                mf = 0
            ans = str(d)[-1] + ans
        if mf == 1:
            ans = '1'+ans
        return ans
        
