'''
https://leetcode.com/problems/multiply-strings/
'''
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(sum(int(num1[i])*int(num2[j])*10**(len(num1)+len(num2)-i-j-2) for i in range(len(num1)) for j in range(len(num2))))
        
