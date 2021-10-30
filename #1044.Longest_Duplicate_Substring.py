'''
https://leetcode.com/problems/longest-duplicate-substring/
'''
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        '''
        ans = ""
        dic = defaultdict(list)
        for i in range(len(s)):
            dic[s[i]] += [i]
        dic = {k:v for k,v in dic.items() if len(v) > 1}
        while 1:
            if len(dic) == 0:
                return ans
            ans = list(dic.keys())[0]
            newdic = defaultdict(list)
            for k,v in dic.items():
                for vi in v:
                    if vi < len(s)-1:
                        newdic[k+s[vi+1]] += [vi+1]
            dic = {k:v for k,v in newdic.items() if len(v) > 1}
        
        for i in range(len(s)-1,0,-1):
            dic = defaultdict(int)
            for j in range(len(s)-i+1):
                dic[s[j:j+i]] += 1
            #print(dic)
            l = [k for k,v in dic.items() if v > 1]
            if len(l) > 0:
                return l[0]
        return ""

        bst = (-1,0)
        for i in range(1,len(s)):
            st,ln = -1,0
            for j in range(len(s)-i):
                #print(j,j+i,s[j],s[j+i],st,ln)
                if s[j] == s[j+i] and st < 0:
                    st = j
                elif s[j] != s[j+i] and st >= 0:
                    ln = j - st
                    if bst[1] < ln:
                        bst = (st,ln)
                    st = -1
            else:
                if st >= 0:
                    ln = len(s) - i - st
                    if bst[1] < ln:
                        bst = (st,ln)
            #print(bst)
            if bst[1] + i >= len(s):
                break
        if bst[1] > 0:
            return s[bst[0]:bst[0]+bst[1]]
        else:
            return ""
        '''
        #别人的答案
        ans = ''
        j   = 1
        for i in range(len(s)):
            longest = s[i:i+j]
            temp    = s[i+1:]
            while longest in temp:
                ans = longest
                j += 1
                longest = s[i:i+j]
        return ans
        
