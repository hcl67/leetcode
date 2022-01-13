'''
https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
'''
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        ans = 0
        points.sort()
        i = 0
        while i < len(points):
            ans += 1
            lst = points[i][1]
            i += 1
            while i < len(points) and lst >= points[i][0]:
                lst = min(lst,points[i][1])
                i += 1                
        return ans
            
        
