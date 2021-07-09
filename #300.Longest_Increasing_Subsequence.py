'''
https://leetcode.com/problems/longest-increasing-subsequence/
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        # O(NlogN)
        import bisect        
        sortedlist = [nums[0]]
        lislist = [[nums[0]]]
        lennums = len(nums)
        for i in range(1,lennums):
            pos = bisect.bisect_left(sortedlist,nums[i])
            if pos == len(sortedlist):
                sortedlist += [nums[i]]
                lislist += [lislist[-1]+[nums[i]]]
            elif pos == 0:
                sortedlist[0] = nums[i]
                lislist[0] = [[nums[i]]]
            else:
                sortedlist[pos] = nums[i]
                lislist[pos] = [lislist[-1]+[nums[i]]]
        return len(sortedlist)
        
        
        '''
        # O(N*2) 
        lennums = len(nums)
        inccnt = [1 for i in range(lennums)]
        for i in range(1,lennums):
                inccnt[i] += max([0] + [inccnt[j] for j in range(i) if nums[i] > nums[j]])
        return max(inccnt)
        '''
