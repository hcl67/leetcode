'''
https://leetcode.com/problems/3sum/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums.sort()
        if nums[0] > 0 or nums[-1] < 0:
            return []
        ans = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            if nums[i] > 0:
                break
            j,k = i+1,len(nums)-1
            while j < k:
                if nums[i] + nums[j] + nums[k] <= 0:
                    if nums[i] + nums[j] + nums[k] == 0:
                        ans += [[nums[i],nums[j],nums[k]]]
                    while j < k:
                        j += 1
                        if nums[j] != nums[j-1]:
                            break
                else:
                    while j < k:
                        k -= 1
                        if nums[k] != nums[k+1]:
                            break
        return ans
            
