'''
https://leetcode.com/problems/student-attendance-record-ii/
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

            
