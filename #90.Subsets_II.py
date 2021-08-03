'''
https://leetcode.com/problems/subsets-ii/
'''
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        '''
        等于给定质因子分解求因子
        '''
        from collections import defaultdict
        pd = defaultdict(int)
        for i in nums:
            pd[i] += 1
        ans = [[]]
        for k,v in pd.items():
            t = [[k] * i for i in range(v+1)]
            ans = [x+y for x in ans for y in t]
        return ans
        
