'''
https://leetcode.com/problems/maximum-subarray/
'''
# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = 0
        maxans = nums[0]
        for n in nums:
            ans = max(n,ans+n)
            maxans = max(maxans,ans)
        return maxans
            
