'''
https://leetcode.com/problems/count-of-smaller-numbers-after-self/
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        import math
        minnum = min(nums)
        maxnum = max(nums)
        numwidth = maxnum - minnum + 1

        rtn = [0] * len(nums)

        #树形求和
        
        def qsumupdate(num, adj, qsumtree):
            qsumdepth = len(qsumtree)
            qsumwidth = len(qsumtree[0]) - 1
            numind = [-1] * qsumdepth
            for l in range(qsumdepth):
                if l == 0:
                    numind[l] = num
                else:
                    binstr = format(num, '0' + str(qsumdepth) + 'b')
                    numind[l] = min(int(binstr[:-l] + '1'*l, 2), qsumwidth)
                qsumtree[l][numind[l]] += adj
            return
            
        def qfirstsum(num, qsumtree):
            if num <= 0:
                return 0
            else:
            #sum first num numbers in qsumstree, i.e. sum [0, num)
                qsumdepth = len(qsumtree)
                qsumwidth = len(qsumtree[0]) - 1
                binstr = format(num, '0' + str(qsumdepth) + 'b')
                pos = 0
                qsum = 0
                for l in range(qsumdepth-1,-1,-1):
                    b = int(binstr[-l-1])
                    if b == 1:
                        pos += 2**(l)
                        qsum += qsumtree[l][pos-1]
                return qsum
    
        
        qsumdepth = int(math.log(numwidth, 2)) + 1
        qsumtree = [[0] * numwidth for i in range(qsumdepth)]
        
        for n in range(len(nums)-1,-1,-1):
            thisnum = nums[n] - minnum
            rtn[n] = qfirstsum(thisnum, qsumtree)
            qsumupdate(thisnum, 1, qsumtree)
        return rtn
            
            
        
        
'''     #求和偷鸡
        lastsum = -1
        lastnum = -1
        for n in range(len(nums)-1,-1,-1):
            thisnum = nums[n] - minnum
            if lastsum >= 0 and thisnum - minnum > abs(thisnum - lastnum):
                if thisnum >= lastnum:
                    thissum = lastsum + sum(cntnum[lastnum:thisnum])
                else:
                    thissum = lastsum - sum(cntnum[thisnum:lastnum])
            else:
                thissum = sum(cntnum[:thisnum])
            cntnum[thisnum] += 1
            
            lastnum = thisnum
            lastsum = thissum
            rtn[n] = thissum
        return rtn
'''
               
