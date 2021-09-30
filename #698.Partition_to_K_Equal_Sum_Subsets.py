'''
https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        s = sum(nums)
        if s % k > 0 :
            return False
        t = s//k
        nums.sort()
        if nums[-1] > t:
            return False
        nums = tuple(nums)
        @cache
        def _t(nums,r): #从nums里凑所有和是t的组合，返回剩余的数字
            ans = []
            for i in range(len(nums)):
                if nums[i] > r:
                    break
                if nums[i] == r:
                    ans += [nums[:i]+nums[i+1:]]
                else:
                    ans += _t(nums[:i]+nums[i+1:],r-nums[i])
            ans.sort()
            return list(ans for ans,_ in itertools.groupby(ans))

        ans = [nums]
        for i in range(k-1):
            newans = []
            for n in ans:
                newans += _t(n,t)
            if newans == []:
                return False
            ans = newans
        return True
