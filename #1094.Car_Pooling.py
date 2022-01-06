'''
https://leetcode.com/problems/car-pooling/
'''
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        car = [0] * 1001
        for t in trips:
            for tt in range(t[1],t[2]):
                car[tt] += t[0]
        return max(car) <= capacity
        
