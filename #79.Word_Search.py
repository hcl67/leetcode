'''
https://leetcode.com/problems/word-search/
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n = len(board),len(board[0])
        st = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if len(word) == 1:
                        return True
                    st.append([(i,j)])
        while st:
            cur = st.pop()
            l = len(cur)
            for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                ni,nj = cur[-1][0]+di, cur[-1][1]+dj
                if 0 <= ni < m and 0 <= nj < n and (ni,nj) not in cur:
                    if board[ni][nj] == word[l]:
                        if len(word) == l+1:
                            return True
                        st.append(cur+[(ni,nj)])
        return False
                    
            
