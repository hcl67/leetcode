'''
https://leetcode.com/problems/isomorphic-strings/
'''
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        maps = {}
        mapt = {}
        for cs,ct in zip(s,t):
            if (cs in maps and ct != maps[cs]) or (ct in mapt and cs != mapt[ct]):
                return False
            else:
                maps[cs] = ct
                mapt[ct] = cs
        return True
        
