'''
https://leetcode.com/problems/student-attendance-record-ii/
'''
'''
1.考虑没有A的情况，三种情况 P, PL, PLL, 有 P(n+1) = P(n)+PL(n)+PLL(n)；PL(n+1)=P(n)；PLL(n+1)=PL(N)
2.考虑加入一个A，是没有A的两侧的乘积
'''
class Solution:
    def checkRecord(self, n: int) -> int:
        K = 10**9+7
        if n == 1:
            return 3
        c = [(1,1,0)]
        s = [2]
        for i in range(1,n):
            c += [((c[-1][0]+c[-1][1]+c[-1][2])%K,c[-1][0]%K,c[-1][1]%K)]
            s += [(c[-1][0]+c[-1][1]+c[-1][2])%K]
        ans = s[-1] + s[-2] * 2
        for i in range(1,n-1):
            ans += s[i-1]*s[n-i-2]
            ans %= K
        return ans

            
