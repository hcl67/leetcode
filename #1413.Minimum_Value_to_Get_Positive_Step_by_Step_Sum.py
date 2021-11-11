'''
https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/
'''
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        ans = [nums[0]]
        for n in nums[1:]:
            ans += [ans[-1]+n]
        return max(-min(ans)+1,1)
        
