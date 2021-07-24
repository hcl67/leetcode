'''
https://leetcode.com/problems/word-ladder-ii/
'''
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        def potw(w):
            from string import ascii_lowercase
            return set([w[:i]+c+w[i+1:] for i in range(len(w)) for c in ascii_lowercase]).difference(w)

        from collections import defaultdict
        if endWord not in wordList:
            return 
        if beginWord not in wordList:
            wordList += [beginWord]
        disdict = defaultdict(list)
        accset = {endWord}
        unaccset = set(wordList).difference(accset)
        flag = 1
        while len(unaccset) > 0 and len(accset) > 0 and flag:
            newaccset = set()
            for wt in accset:
                whset = unaccset.intersection(potw(wt))
                if beginWord in whset:
                    flag = 0
                for wh in whset:
                    disdict[wh] += [wt]
                newaccset.update(whset)
            unaccset.difference_update(newaccset)
            accset = newaccset
        if beginWord in unaccset:
            return
#        print(disdict)
        ans = [[beginWord]]
        while 1:
            ans = [x+[y] for x in ans for y in disdict[x[-1]]]
            if ans[0][-1] == endWord:
                break
#        print(ans)
        return ans
        
        
'''
        def worddis(w1,w2):
            return sum(0 if w1[k] == w2[k] else 1 for k in range(len(w1)))
        
        from collections import defaultdict
        if endWord not in wordList:
            return 
        if beginWord not in wordList:
            wordList += [beginWord]
        disdict = defaultdict(list)
        accset = {endWord}
        unaccset = set(wordList).difference(accset)
        flag = 1
        while len(unaccset) > 0 and len(accset) > 0 and flag:
            newaccset = set()
            for wt in accset:
                for wh in unaccset:
                    if worddis(wt,wh) == 1:
                        disdict[wh] += [wt]
                        newaccset.add(wh)
                        if wh == beginWord:
                            flag = 0
            unaccset.difference_update(newaccset)
            accset = newaccset
        if beginWord in unaccset:
            return
    #    print(disdict)
        ans = [[beginWord]]
        while 1:
            ans = [x+[y] for x in ans for y in disdict[x[-1]]]
            if ans[0][-1] == endWord:
                break
    #    print(ans)
        return ans
'''        
                   
        
        
