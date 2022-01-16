'''
https://leetcode.com/problems/maximize-distance-to-closest-person/
'''
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans,tmp = 0,-1
        for i in range(len(seats)):
            if seats[i] == 1:
                if tmp == -1:
                    tmp = i
                    ans = i
                else:
                    ans = max(ans,(i-tmp)//2)
                    tmp = i
        ans = max(ans,len(seats)-1-tmp)
        return ans
