'''
https://leetcode.com/problems/number-of-valid-words-for-each-puzzle/
'''
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        '''
        ps,ws = [set(p) for p in puzzles],[set(w) for w in words]
        return [sum(1 for j in range(len(words)) if puzzles[i][0] in ws[j] and len(ws[j] - ps[i]) == 0) for i in range(len(puzzles))]
        
        def _bs(s):
            return reduce(lambda x,y: x|y,[2**(ord(c)-97) for c in s])
        p1,ps,ws = [_bs(p[0]) for p in puzzles],[_bs(p) for p in puzzles],[_bs(w) for w in words]
        return [sum(p1[i]&ws[j]>0 and (ps[i]^ws[j])&ws[j]==0 for j in range(len(words))) for i in range(len(puzzles))]

        
        #将将可以过
        pd = defaultdict(set)
        for i in range(len(puzzles)):
            for c in puzzles[i]:
                pd[c].add(i)
        ans = [0]*len(puzzles)
        for w in words:
            a0 = set.intersection(*[pd[c] for c in w])
            for i in a0:
                if puzzles[i][0] in w:
                    ans[i]+=1
        return ans
        '''
        #答案后的改造
        def _bs(s):
            return reduce(lambda x,y: x|y,[1<<(ord(c)-97) for c in s])
        wf = Counter([_bs(w) for w in words])
        ans = []
        for p in puzzles:
            total = 0
            for choose in range(1 << 6):
                mask = 0
                for i in range(6):
                    if choose & (1 << i):
                        mask |= (1 << (ord(p[i + 1]) - 97))
                mask |= (1 << (ord(p[0]) - 97))
                if mask in wf:
                    total += wf[mask]
            ans += [total]
        return ans
