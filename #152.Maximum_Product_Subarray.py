'''
https://leetcode.com/problems/maximum-product-subarray/
'''
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        def _c(cur):
            if len(cur) == 0:
                return -inf
            if len(cur) == 1:
                return cur[0]
            pcur = math.prod(cur)
            if pcur > 0:
                return pcur
            t0,t1 = 1,1
            for i in range(len(cur)):
                t0 *= cur[i]
                if t0 < 0:
                    break
            for i in range(len(cur)-1,-1,-1):
                t1 *= cur[i]
                if t1 < 0:
                    break
            return max(pcur//t0,pcur//t1)
        
        ans = -inf
        cur = [] 
        for n in nums:
            if n == 0:
                ans = max(ans,_c(cur),0)
                cur = []
            else:
                cur.append(n)
        else:
            ans = max(ans,_c(cur))
        return ans    
                
            
        
