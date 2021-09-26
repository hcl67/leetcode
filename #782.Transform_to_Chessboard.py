'''
https://leetcode.com/problems/transform-to-chessboard/
'''
class Solution:
    def movesToChessboard(self, board: List[List[int]]) -> int:
        #满足条件的矩阵必然n//2行一致，剩余n//2正交
        n = len(board)
        r0 = board[0]
        i0 = [1-x for x in r0]
        c0 = [1]
        if n%2 ==0:
            if sum(r0) != n//2:
                return -1
            for i in range(1,n):
                if board[i] == r0:
                    c0 += [1]
                elif board[i] == i0:
                    c0 += [0]
                else:
                    return -1
            if sum(c0) != n//2:
                return -1
            sr = sum(r0[i] if i%2 == 0 else 0 for i in range(n))
            sc = sum(c0[i] if i%2 == 0 else 0 for i in range(n))
            return min(sr,n//2-sr)+min(sc,n//2-sc)
        else:
            dr = sum(r0) - n//2
            if dr not in {0,1}:
                return -1
            for i in range(1,n):
                if board[i] == r0:
                    c0 += [1]
                elif board[i] == i0:
                    c0 += [0]
                else:
                    return -1
            dc = sum(c0) - n//2
            if dc not in {0,1}:
                return -1
            sr = sum(r0[i] if i%2 == dr else 0 for i in range(n))
            sc = sum(c0[i] if i%2 == dc else 0 for i in range(n))                    
            return sr+sc
            
