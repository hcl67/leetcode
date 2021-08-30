'''
https://leetcode.com/problems/range-addition-ii/
'''
class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a = m
        b = n
        for i in range(len(ops)):
            a = min(ops[i][0],a)
            b = min(ops[i][1],b) 
        return a*b
        
