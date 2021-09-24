'''
https://leetcode.com/problems/n-th-tribonacci-number/
'''
class Solution:
    def tribonacci(self, n: int) -> int:
        '''
        x = 1.83928675521416
        y = complex(-0.419643377607081,-0.606290729207199)
        z = complex(-0.419643377607081,0.606290729207199)
        a = 1/(-x*x+4*x-1)
        b = 1/(-y*y+4*y-1)
        c = 1/(-z*z+4*z-1)
        return round((a*x**n+b*y**n+c*z**n).real)
        '''
        t = [0,1,1]
        i = 3
        while i<=n:
            t[i%3] += t[(i-1)%3] + t[(i-2)%3]
            i += 1
        return t[n%3]
