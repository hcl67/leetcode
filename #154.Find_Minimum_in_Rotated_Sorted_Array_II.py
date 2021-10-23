'''
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
'''
class Solution:
    def findMin(self, nums: List[int]) -> int:
        def _fm(nums):
            if len(nums) == 1:
                return nums[0]
            elif len(nums) == 2:
                return min(nums)
            if nums[0] < nums[-1]:
                return nums[0]
            else:
                k = len(nums)//2
                if nums[0] == nums[k-1] == nums[-1]:
                    return min(_fm(nums[:k]),_fm(nums[k:]))
                elif nums[0] <= nums[k-1]:
                    return _fm(nums[k:])
                else:
                    return _fm(nums[:k])
        return _fm(nums)
