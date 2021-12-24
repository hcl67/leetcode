'''
https://leetcode.com/problems/merge-intervals/
'''
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x:x[0])
        ans = [intervals[0]]
        for curinv in intervals[1:]:
            lstinv = ans[-1]
            if curinv[0] <= lstinv[1]:
                lstinv[1] = max(curinv[1],lstinv[1])
            else:
                ans.append(curinv)
        return ans
            
        
