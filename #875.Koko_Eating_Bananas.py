'''
https://leetcode.com/problems/koko-eating-bananas/
'''
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def _c(piles,k):
            return sum((p+k-1)//k for p in piles)
        if h == len(piles):
            return max(piles)   
        if h >= sum(piles):
            return 1
        mxk, mnk = max(piles), 1
        while 1:
            if mxk - mnk == 1:
                return mxk
            mdk = (mxk + mnk) // 2
            if  _c(piles, mdk) <= h:
                mxk = mdk
            else:
                mnk = mdk        
        
        
 
