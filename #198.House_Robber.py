'''
https://leetcode.com/problems/house-robber/
'''
class Solution:
    def rob(self, nums: List[int]) -> int:
        r,n = nums[0],0
        for m in nums[1:]:
            n,r = max(n,r),m+n
        return max(r,n)
