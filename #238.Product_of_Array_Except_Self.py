'''
https://leetcode.com/problems/product-of-array-except-self/
'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        pre,suf = [1]*len(nums),[1]*len(nums)
        for i in range(1,len(nums)):
            pre[i] = pre[i-1]*nums[i-1]
            suf[i] = suf[i-1]*nums[-i]
        suf = suf[::-1]
        return [pre[i]*suf[i] for i in range(len(nums))]
        '''
        pre,suf = 1,1
        ans = [1]*len(nums)
        for i in range(1,len(nums)):
            pre *= nums[i-1]
            ans[i] *= pre
            suf *= nums[-i]
            ans[-i-1] *= suf
        return ans
            
            
