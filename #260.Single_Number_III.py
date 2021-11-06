'''
https://leetcode.com/problems/single-number-iii/
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        '''
        d = {}
        for i in nums:
            if i in d:
                del d[i]
            else:
                d[i] = 1
        return list(d.keys())
        '''
        #看答案提示后
        x = 0
        for n in nums:
            x ^= n
        f = 1
        while x&f == 0:
            f<<=1
        x,y = 0,0
        for n in nums:
            if n&f:
                x ^= n
            else:
                y ^= n
        return [x,y]
