'''
https://leetcode.com/problems/max-consecutive-ones-iii/
'''

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        #改造序列压缩1
        modnums = []
        cum1 = 0
        for n in range(len(nums)):
            if nums[n] == 0 and cum1 == 0:
                modnums += [0]
            elif nums[n] == 0 and cum1 > 0:
                modnums += [cum1, 0]
                cum1 = 0
            else:
                cum1 +=1
        if cum1 > 0:
            modnums += [cum1]
#        print(modnums)
                
        if k == 0:
            return max(modnums)
        elif modnums.count(0) < k:
            return len(nums)
        
        ind0 = []
        maxl = 0
        curl = 0
        for n in range(len(modnums)):
            if modnums[n] > 0:
                curl += modnums[n]
            else:
                if len(ind0) < k:
                    ind0 += [n]
                    curl += 1
                else:
                    maxl = max(maxl, curl)
                    if ind0[0] > 0:
                        curl -= modnums[ind0[0] - 1]
                    del ind0[0]
                    ind0 += [n]
        
#            print(ind0)
#            print(maxl)
        
        return max(maxl, curl)
        
        
        
'''
注意到为了最大化连续1的数量，0必然是连在一起的（跳过1），故构造k长度0的index队列，扫nums进出，求max头尾index差
'''
