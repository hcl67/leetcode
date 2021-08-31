'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        while j>i:
            mid = (i+j)//2
            if nums[mid]<nums[j]:
                j = mid
            else:
                i = mid + 1
        return nums[i]
                
