'''
https://leetcode.com/problems/sort-colors/
'''
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c = Counter(nums)
        nums[:c[0]] = [0]*c[0]
        nums[c[0]:c[0]+c[1]] = [1]*c[1]
        nums[c[0]+c[1]:] = [2]*c[2]
        
        
