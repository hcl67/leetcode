'''
https://leetcode.com/problems/find-peak-element/
'''
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if len(nums) == 1:
            return 0
        elif nums[0] > nums[1]:
            return 0
        elif nums[n-1] > nums[n-2]:
            return n-1
        else:
            a = 0
            b = n-1
            while(1):
                c = (a+b)//2            
                if nums[c] > nums[c-1] and nums[c] > nums [c+1]:
                    return c
                elif nums[c] < nums[c-1]:
                    b = c
                else:
                    a = c
        
