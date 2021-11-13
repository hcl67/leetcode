'''
https://leetcode.com/problems/daily-temperatures/
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        td = defaultdict(list)
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            t = temperatures[i]
            for k,v in list(td.items()):
                if k < t:
                    for iv in v:
                        ans[iv] = i - iv
                    del td[k]
            td[t] += [i]
        return ans
        
