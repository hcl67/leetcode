'''
https://leetcode.com/problems/nth-magical-number/
'''
class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ab = a*b//math.gcd(a,b)
        cy = ab//a + ab//b - 1
        nd,nr = n//cy , n%cy
        r = sorted(list(range(0,ab,a))+list(range(0,ab,b)))[nr+1]
        return (nd*ab+r)%(10**9+7)
        
