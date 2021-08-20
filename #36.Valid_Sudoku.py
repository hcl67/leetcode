'''
https://leetcode.com/problems/valid-sudoku/
'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rc = [[] for k in range(9)]
        cc = [[] for k in range(9)]
        bc = [[] for k in range(9)]
        for i in range(9):
            for j in range(9):
                x = board[i][j]
                if x != '.':
                    rc[i] += [x]
                    cc[j] += [x]
                    bc[i//3*3+j//3] += [x]
        for k in range(9):
            if len(set(rc[k])) < len(rc[k]) or len(set(cc[k])) < len(cc[k]) or len(set(bc[k])) < len(bc[k]):
                return False
        return True
