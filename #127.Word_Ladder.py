'''
https://leetcode.com/problems/word-ladder/
'''
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        if endWord == beginWord:
            return 1
        n = len(beginWord)
        wd = defaultdict(set)
        for w in [beginWord]+wordList:
            for i in range(n):
                wd[w[:i]+'_'+w[i+1:]].add(w)
        q = deque([[beginWord]])
        usedw = set([beginWord])
        while q:
            cur = q.popleft()
            lstw = cur[-1]
            for i in range(n):
                neww = wd[lstw[:i]+'_'+lstw[i+1:]]-usedw
                if endWord in neww:
                    return len(cur) + 1
                usedw |= neww
                for w in neww:
                    q.append(cur+[w])
        return 0
            
                    
        
