'''
https://leetcode.com/problems/find-winner-on-a-tic-tac-toe-game/
'''
class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        def check(move):
            if [0,0] in move:
                if [0,1] in move and [0,2] in move or [1,0] in move and [2,0] in move or [1,1] in move and [2,2] in move:
                    return True
            if [0,1] in move:
                if [1,1] in move and [2,1] in move:
                    return True
            if [0,2] in move:
                if [1,2] in move and [2,2] in move or [1,1] in move and [2,0] in move:
                    return True
            if [1,0] in move:
                if [1,1] in move and [1,2] in move:
                    return True
            if [2,0] in move:
                if [2,1] in move and [2,2] in move:
                    return True
            return False
        
        moveA,moveB = [],[]
        for i in range(len(moves)):
            if i%2 == 0:
                moveA += [moves[i]]
            else:
                moveB += [moves[i]]
        if check(moveA):
            return 'A'
        elif check(moveB):
            return 'B'
        elif len(moves) <9:
            return "Pending"
        else:
            return "Draw"
                    
