'''
https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        setl = [set()]
        for x in arr:
            setx = set(x)
            if len(setx) < len(x):
                continue
            newsetl = setl
            for y in setl:
                if len(set.intersection(setx,y)) == 0:
                    newsetl += [set.union(setx,y)]
            setl = newsetl
        return max([len(x) for x in setl])
        
