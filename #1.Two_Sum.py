'''
https://leetcode.com/problems/two-sum/
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sortednums = sorted(nums)
        i = 0
        j = len(nums) - 1
        while i < j:
            if sortednums[i] + sortednums[j] < target:
                i += 1
            elif sortednums[i] + sortednums[j] > target:
                j -= 1
            else:
                return [nums.index(sortednums[i]), len(nums) -1 - nums[::-1].index(sortednums[j])]
