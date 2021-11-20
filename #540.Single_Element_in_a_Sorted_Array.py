'''
https://leetcode.com/problems/single-element-in-a-sorted-array/
'''
class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        '''
        return reduce(lambda x,y:x^y,nums)
        '''
        
        i,j = 0,len(nums)-1
        while i<j:
            k = (i+j)//2
            if nums[k-1] != nums[k] and nums[k] != nums[k+1]:
                return nums[k]
            elif nums[k-1] == nums[k] and k % 2 == 0:
                    j = k
            elif nums[k] == nums[k+1] and k % 2 == 1:
                    j = k - 1
            elif nums[k-1] == nums[k] and k % 2 == 1:
                    i = k + 1
            elif nums[k] == nums[k+1] and k % 2 == 0:
                    i = k
                
        return nums[i]
