'''
https://leetcode.com/problems/word-search-ii/
'''
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:    
        
        m,n = len(board),len(board[0])
        
        adjdict = {}
        worddict = defaultdict(list)
        for i in range(m):
            for j in range(n):
                adjdict[(i,j)] = {}
                worddict[board[i][j]] += [((i,j),)]
                for di,dj in [(1,0),(-1,0),(0,1),(0,-1)]:
                    ni,nj = i+di, j+dj
                    if 0 <= ni < m and 0 <= nj < n:
                        adjdict[(i,j)][(ni,nj)] = board[i][j]+board[ni][nj]
                                              
#        @cache
        def nexts(s,w):
            ns = []
            qk = s[-1]
            qv = board[qk[0]][qk[1]]+w
            for k,v in adjdict[qk].items():
                if v == qv and k not in s:
                    ns += [s+(k,)]
            return ns
        
        @cache
        def pre(w):
            if len(w) == 1:
                return [x for x in worddict[w]]
            else:
                st = pre(w[:-1])
                ns = []
                for s in st:
                    ns += nexts(s,w[-1])
                return ns
        @cache    
        def pre(w):
            if len(w) == 1:
                return [x for x in worddict[w]]
            else:
                st = pre(w[:-1])
                ns = []
                for s in st:
                    ns += nexts(s,w[-1])
                return ns

        def exist(word):
            if len(word) == 1:
                if pre(word):
                    return True
                else:
                    return False
            st = pre(word[:-1])
            for s in st:
                if nexts(s,word[-1]):
                    return True
            return False
        
        ans = []
        for w in words:
            if exist(w):
                ans += [w]
        return ans
