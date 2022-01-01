'''
https://leetcode.com/problems/burst-balloons/
'''
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        '''
        TLE
        @cache
        def _c(lst):
            if len(lst) == 1:
                return lst[0]
            if len(lst) == 2:
                return lst[0]*lst[1]+max(lst)
            else:
                lst = tuple([1] + list(lst) + [1])
                return max([_c(lst[1:i]+lst[i+1:-1]) + lst[i-1]*lst[i]*lst[i+1] for i in range(1,len(lst)-1)])
        lst = tuple([x for x in nums if x > 0])
        return _c(lst)
        '''
        # Once we tried a certain balloon as the last one to be bursted, before it is bursted, its left and right sides are not connected.
        @cache
        def search(nums):
            return 0 if len(nums) < 3 else max([search(nums[:i + 1]) + search(nums[i:]) 
			        + nums[0] * nums[i] * nums[-1] for i in range(1, len(nums) - 1)])
        return search(tuple([1] + nums + [1]))
