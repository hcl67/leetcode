'''
https://leetcode.com/problems/palindrome-partitioning-ii/
'''
class Solution:
    def minCut(self, s: str) -> int:
        def pld(s):
            return s == s[::-1]
        
        ans = [0] * (len(s))
        for j in range(1,len(s)):
            bst = ans[j-1]+1
            for i in range(j):
                if pld(s[i:j+1]):
                    if i == 0:
                        bst = 0
                    else:
                        bst = min(bst, ans[i-1]+1)
            ans[j] = bst
        return ans[-1]         
