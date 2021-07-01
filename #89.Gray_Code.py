'''
https://leetcode.com/problems/gray-code/
'''
class Solution:
    def grayCode(self, n: int) -> List[int]:
        l = [0,1]
        for i in range(1,n):
            l += [x + 2**i for x in l[::-1]]
        return l
        
