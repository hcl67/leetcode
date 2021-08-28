'''
https://leetcode.com/problems/maximum-profit-in-job-scheduling/
'''
class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        step=sorted(set(startTime+endTime))
        totProfit={step[0]:0}
        check=defaultdict(list)
        for i in range(len(endTime)):
            check[endTime[i]]+=[(startTime[i],profit[i])]
        for i in range(1,len(step)):
            #print(totProfit,step[i-1],step[i])
            maxpft=totProfit[step[i-1]]
            for j in check[step[i]]:
                maxpft=max(maxpft,totProfit[j[0]]+j[1])
            totProfit[step[i]]=maxpft
            #print(maxpft)
        return totProfit[step[-1]]
