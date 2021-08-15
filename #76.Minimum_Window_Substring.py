class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tc = Counter(t)
        ans = ''
        i = 0
        while s[i] not in tc:
            i += 1
            if i >= len(s):
                return ''
        j = i
        tc[s[i]] -= 1
        while 1:
            if j == len(s)-1 and len([1 for v in tc.values() if v>0])>0:
                break
            elif len([1 for v in tc.values() if v>0])>0:
                j += 1
                while s[j] not in tc and j < len(s) - 1:
                    j += 1
                if s[j] in tc:
                    tc[s[j]] -= 1
            elif len([1 for v in tc.values() if v>0])==0:
                if ans == '' or len(s[i:j+1])<len(ans):
                    ans = s[i:j+1]
                while s[i] not in tc:
                    i += 1
                tc[s[i]] += 1
                i += 1
        return ans            
'''       
        def cont(tc,sc):
            return len([1 for d in tc.keys() if tc[d]>sc[d]]) == 0
        tc = Counter(t)
        sc = defaultdict(int)

        ans = ''
        i = j = 0
        sc[s[i]] += 1
        while 1:
            if j == len(s)-1 and not cont(tc,sc):
                break
            elif not cont(tc,sc):
                j += 1
                sc[s[j]] += 1
            elif cont(tc,sc):
                if ans == '' or len(s[i:j+1])<len(ans):
                    ans = s[i:j+1]
                sc[s[i]] -= 1
                i += 1
        return ans 
'''         
