'''
https://leetcode.com/problems/orderly-queue/
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        #当k>=2时，可以视作冒泡排序
        if k == 1:
            l = []
            for i in range(len(s)):
                s = s[1:]+s[:1]
                l += [s]
            return min(l)        
        else:
            return ''.join(sorted(s))     
        
