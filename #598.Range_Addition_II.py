'''
https://leetcode.com/problems/range-addition-ii/
'''

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        a,b = m,n
        for op in ops:
            a,b = min(op[0],a),min(op[1],b)
        return a*b
        
