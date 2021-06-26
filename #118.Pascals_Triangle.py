'''
https://leetcode.com/problems/pascals-triangle/
'''
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        p = [[1]]
        if numRows == 1:
            return p
        else:
            for i in range(1, numRows):
                p_i = [1]
                for j in range(1, i):
                    p_i += [p[i-1][j-1] + p[i-1][j]]
#                    print(p_i)
                p_i += [1]
                p += [p_i]
            return p
