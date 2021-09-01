'''
https://leetcode.com/problems/array-nesting/
'''
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n=0
        i=0
        d=[]
        while 1:
            t=i
            ni=1
            while nums[t]!=i:
                tt=nums[t]
                nums[t]=i
                t=tt
                ni+=1
            #print(nums,ni)
            n+=ni
            i+=1
            d+=[ni]
            if n>=len(nums):
                break
            while i>nums[i]:
                i+=1
        return max(d)
        
