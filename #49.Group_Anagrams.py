'''
https://leetcode.com/problems/group-anagrams/
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        strd = defaultdict(list)
        for s in strs:
            strd["".join(sorted(s))] += [s]
        return list(strd.values())
        
