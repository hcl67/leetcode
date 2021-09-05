'''
https://leetcode.com/problems/orderly-queue/
'''
class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        #当k>=2时，可以视作冒泡排序
        if k == 1:
            c = min(list(s))
            i = s.find(c)
            l = [c+s[i+1:]+s[:i]]
            while 1:
                i = s.find(c,i+1)
                if i < 0:
                    break
                l += [c+s[i+1:]+s[:i]]
            return min(l)            
        else:
            return ''.join(sorted(s))
        
