'''
https://leetcode.com/problems/word-pattern/
'''
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        return len(pattern) == len(l := s.split()) and len(set(pattern)) == len(set(l)) == len(set((pattern[i],l[i]) for i in range(len(pattern))))
