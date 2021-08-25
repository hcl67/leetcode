class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        b = isqrt(c)
        while a<=b:
            ab = a**2 + b**2
            if ab == c:
                return True
            elif ab > c:
                b -= 1
            else:
                a += 1
        return False
        
