'''
https://leetcode.com/problems/jump-game/
'''
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        i = len(nums)-1
        while i>0:
            jp = 0
            for j in range(i-1,-1,-1):
                #print(j,nums[j],i)
                if j+nums[j]>=i:
                    jp = 1
                    break
            if jp == 0:
                return False
            i = j
        if jp == 1:
            return True
        else:
            return False
            
