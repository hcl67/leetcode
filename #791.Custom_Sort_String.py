'''
https://leetcode.com/problems/custom-sort-string/
'''
class Solution:
    def customSortString(self, order: str, str: str) -> str:
        from collections import defaultdict
        orderset = set(order)
        strdict = defaultdict(int)
        ans = ''
        for c in str:
            if c in orderset:
                strdict[c] += 1
            else:
                ans += c
        for c in order:
            ans += c * strdict[c]
        return ans
                
