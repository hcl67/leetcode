'''
https://leetcode.com/problems/surrounded-regions/
'''
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        updo,vewo = set(),set()
        updo.update({(i,j) for i in [0,len(board)-1] for j in range(len(board[0])) if board[i][j] == 'O'})
        updo.update({(i,j) for j in [0,len(board[0])-1] for i in range(len(board)) if board[i][j] == 'O'})
        while len(updo)>0:
            #print(updo)
            curo = updo.pop()
            vewo.add(curo)
            for d in [(1,0),(-1,0),(0,1),(0,-1)]:
                tmp = (curo[0]+d[0],curo[1]+d[1])
                if 0 <= tmp[0] < len(board) and 0 <= tmp[1] < len(board[0]) and board[tmp[0]][tmp[1]] == 'O' and tmp not in vewo and tmp not in updo:
                    updo.add(tmp)
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i,j) not in vewo:
                    board[i][j] = 'X'
        return
                    
                    
        
