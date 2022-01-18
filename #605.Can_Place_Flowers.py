'''
https://leetcode.com/problems/can-place-flowers/solution/
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        newbed = [1,0] + flowerbed + [0,1]
        cn,tn = 0,0
        for c in newbed:
            #print(c,cn,tn)
            if c == 0:
                cn += 1
            else:
                tn += max((cn-1)//2, 0)
                cn = 0
        return tn >= n
        
