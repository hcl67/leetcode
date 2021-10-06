'''
https://leetcode.com/problems/find-all-duplicates-in-an-array/
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            if nums[i] <= 0:
                continue
            d = nums[i]
            nums[i] = 0
            while d > 0:
                t = d - 1
                d = nums[t]
                if nums[t] > 0:
                    nums[t] = -1
                else:
                    nums[t] -= 1
        return [i+1 for i in range(len(nums)) if nums[i] == -2]
