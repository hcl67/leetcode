'''
https://leetcode.com/problems/largest-divisible-subset/
'''
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        ansl = []
        nums.sort()
        for i in range(len(nums)):
            ansl += [[nums[i]]]
            for j in range(i-1,-1,-1):
                if nums[i] % nums[j] == 0:
                    if len(ansl[j]) + 1 > len(ansl[i]):
                        ansl[i] = ansl[j]+[nums[i]]
        return max(ansl,key=len)
