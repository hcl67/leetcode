'''
https://leetcode.com/problems/partition-array-into-disjoint-intervals/
'''

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        rmin = [0]*n
        rmin[n-1] = nums[n-1]
        for i in range(n-2,-1,-1):
            rmin[i] = min(nums[i],rmin[i+1])
        lmax = 0
        for i in range(n-1):
            lmax = max(lmax,nums[i])
            if lmax <= rmin[i+1]:
                break
        return i+1
