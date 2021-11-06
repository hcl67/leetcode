'''
https://leetcode.com/problems/single-number-iii/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        d = {}
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i] = 1
        return list(d.keys())
        
