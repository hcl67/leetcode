'''
https://leetcode.com/problems/kth-smallest-number-in-multiplication-table/
'''

'''
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def _c(x):
            return sum(min(x//i,m) for i in range(1,min(x,n)+1))
        
        def _d(x):
            return min(x%i if i*n>=x else 999999 for i in range(1,m+1))
        
        if k == 1:
            return 1
        if k == m*n:
            return m*n
        ma,mc = 1,m * n
        while mc-1-_d(mc-1) > ma:
            mb = (ma+mc)//2
            mb -= _d(mb)
            if _c(mb) >= k:
                mc = mb
            else:
                if ma == mb:
                    break
                ma = mb
        d = mc
        while 1:
            dd = d-1-_d(d-1)
            if _c(dd)<k:
                return d
            d = dd
'''
# 实际上，看答案后发现，由于寻找的是满足条件的下限，所以必然会找到表中的点，代码可以简化为：
class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        def _c(x):
            return sum(min(x//i,m) for i in range(1,min(x,n)+1))
        
       
        if k == 1:
            return 1
        if k == m*n:
            return m*n
        ma,mc = 1,m * n
        while mc > ma:
            mb = (ma+mc)//2
            if _c(mb) >= k:
                mc = mb
            else:
                ma = mb+1
        return ma
