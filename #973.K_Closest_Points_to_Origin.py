'''
https://leetcode.com/problems/k-closest-points-to-origin/
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        from sortedcontainers import SortedList
        ans = SortedList()
        for p in points:
            ans.add([p[0]**2+p[1]**2,p])
            if len(ans) > k:
                ans.pop()
        return [i[1] for i in ans]
        '''
        #本质还是排序
        return sorted(points,key=lambda p:p[0]**2+p[1]**2)[:k]
        
