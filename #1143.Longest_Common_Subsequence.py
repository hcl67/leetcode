'''
https://leetcode.com/problems/longest-common-subsequence/
'''
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if len(text1) < len(text2):
            text1,text2 = text2,text1
        dt1 = defaultdict(list)
        for i in range(len(text1)):
            dt1[text1[i]] += [i]
        dt2 = []
        for c in text2:
            if c not in dt1:
                continue
            cp = dt1[c]
            for j in range(len(dt2)-1,-1,-1):
                acp = [p for p in cp if p > dt2[j]]
                if len(acp) > 0:
                    if j == len(dt2)-1:
                        dt2 += [acp[0]]
                    elif dt2[j+1] > acp[0]:
                        dt2[j+1] = acp[0]
            if len(dt2) == 0:
                dt2 += [cp[0]]
            elif dt2[0] > cp[0]:
                dt2[0] = cp[0]
                
        return len(dt2)
                
