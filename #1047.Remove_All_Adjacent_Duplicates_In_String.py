'''
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
'''

class Solution:
    def removeDuplicates(self, s: str) -> str:
        r = ""
        for c in s:
            if len(r) > 0 and r[-1] == c:
                r = r[:-1]
            else:
                r += c
        return r
        
