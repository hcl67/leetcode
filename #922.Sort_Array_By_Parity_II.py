'''
https://leetcode.com/problems/sort-array-by-parity-ii/
'''
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        '''
        nums.sort(key=lambda x:x%2)
        return [nums[i//2] if i%2 ==0 else nums[-(i//2+1)] for i in range(len(nums))]
        '''
        ans = [0]*len(nums)
        i,j = 0,1
        for x in nums:
            if x%2 == 0:
                ans[i] = x
                i+=2
            else:
                ans[j] = x
                j+=2
        return ans
