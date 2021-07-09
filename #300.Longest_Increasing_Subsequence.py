'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #N^2 trial
        lennums = len(nums)
        inccnt = [1 for i in range(lennums)]
        for i in range(1,lennums):
                inccnt[i] += max([0] + [inccnt[j] for j in range(i) if nums[i] > nums[j]])
        return max(inccnt)
