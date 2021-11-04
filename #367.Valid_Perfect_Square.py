'''
https://leetcode-cn.com/problems/valid-perfect-square/
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i,j = 1,2**16
        while j-i>1:
            if i**2 == num or j**2 == num:
                return True
            else:
                k = (i+j)//2
                if k**2 >= num:
                    j = k
                else:
                    i = k
        if i**2 == num or j**2 == num:
            return True
        else:
            return False
            
