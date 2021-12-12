'''
https://leetcode.com/problems/partition-equal-subset-sum/
'''
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        target = sum(nums)
        if target&1:
            return False
        target >>= 1
        counter = Counter(nums)
        can = set([0])
        for k,v in counter.items():
            apd = set()
            for j in can:
                apd |= set(j+i*k for i in range(1,v+1))
            can |= apd
            if target in can:
                return True
        return False
        '''
        target = sum(nums)
        if target&1:
            return False
        target >>= 1
        can = set([0])
        for i in nums:
            apd = set()
            for j in can:
                apd.add(i+j)
            can |= apd
            if target in can:
                return True
        return False        
        
        
        
        '''
        TLE
        for i in range(1<<(len(nums)-1)):
            t = 0
            k = i
            for j in range(len(nums)):
                if k&1:
                    t += nums[j] 
                k >>= 1
                if t == s:
                    return True
                if t > s:
                    break
        return False
        '''
