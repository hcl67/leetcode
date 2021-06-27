'''
https://leetcode.com/problems/candy/
'''
class Solution:
    def candy(self, ratings: List[int]) -> int:
        sumcandy = 0
        pos = 0
        curcandy = 1
        tot = len(ratings) - 1
        while(pos<tot):
            if ratings[pos] == ratings[pos+1]:
                sumcandy += curcandy
                pos += 1
                curcandy = 1
            elif ratings[pos] < ratings[pos+1]:
                sumcandy += curcandy
                pos += 1
                curcandy += 1
            else:
                cntgt = 0
                while(pos<tot):
                    if ratings[pos] <= ratings[pos+1]:
                        break
                    cntgt += 1
                    pos += 1
                if curcandy > cntgt:
                    sumcandy += curcandy + cntgt*(cntgt+1)//2 - 1  #当前位置的,1candy,不用加
                else:
                    sumcandy += (cntgt+1)*(cntgt+2)//2 - 1  #当前位置的,1candy,不用加
                curcandy = 1
        sumcandy += curcandy    
        return sumcandy
