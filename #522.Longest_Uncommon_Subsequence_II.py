'''
https://leetcode.com/problems/longest-uncommon-subsequence-ii/
'''
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        #按照长度降序，依次判断所有count为1的字符串是不是是更长的count>1的字符串的子序列
        def issubsq(sub, ori):
            i = 0
            for j in range(len(ori)):
                if sub[i] == ori[j]:
                    i += 1
                if i == len(sub):
                    return True
            return False


        from collections import defaultdict
        from functools import reduce
        counter = defaultdict(int)
        mulpool = defaultdict(set)
        unipool = defaultdict(set)
        for k in strs:
            counter[k] += 1
        for k,v in counter.items():
            if v == 1:
                unipool[len(k)].add(k)
            else:
                mulpool[len(k)].add(k)
        mulkeys,unikeys = sorted(list(mulpool.keys()),reverse=True), sorted(list(unipool.keys()),reverse=True)
        if len(unikeys) == 0:
            return -1
        if len(mulkeys) == 0 or mulkeys[0] <= unikeys[0]:
            return unikeys[0]
        for uk in unikeys:
            ukmp = reduce(lambda x,y: x.union(y),[mulpool[mk] for mk in mulkeys if mk > uk])
            for ustr in unipool[uk]:
                trial = 0
                for mstr in ukmp:
                    if issubsq(ustr, mstr):
                        trial = 1
                        break
                if trial == 0:
                    return uk
        return -1
                    
