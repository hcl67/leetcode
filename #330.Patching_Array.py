'''
https://leetcode.com/problems/patching-array/
'''
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        ans = 0
        i = 1
        if nums[0] != 1:
            ans += 1
            i -= 1
        cap = 1
        while cap < n:
            if i >= len(nums):
                while cap < n:
                    cap += cap + 1
                    ans += 1
            elif nums[i] <= cap + 1:
                cap += nums[i]
                i += 1
            else:
                while nums[i] > cap + 1 and cap < n:
                    cap += cap + 1
                    ans += 1
        return ans
        
