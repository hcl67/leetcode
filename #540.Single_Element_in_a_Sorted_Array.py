'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        return reduce(lambda x,y:x^y,nums)
        
