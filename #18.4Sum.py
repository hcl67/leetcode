'''
https://leetcode.com/problems/4sum/
'''
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        from collections import defaultdict
        if len(nums) < 4:
            return []
        dict_pre = defaultdict(int)
        for i in nums:
            dict_pre[i] += 1
        nums2 = []
        for k in sorted(list(dict_pre.keys())):
            nums2 += [k]*min(4,dict_pre[k])
        if len(nums2) == 4 and sum(nums2) == target:
            return [nums2]
        elif len(nums2) == 4:
            return []
        sum2dict = defaultdict(set)
        for i in range(len(nums2)-1):
            for j in range(i+1,len(nums2)):
                sum2 = nums2[i] + nums2[j]
                sum2dict[sum2].add((i,j,nums2[i],nums2[j]))
        sum2list = sorted(list(sum2dict.keys()))
        i = 0
        j = len(sum2list)-1
        potlist = []
        while(j>=i):
            if sum2list[i] + sum2list[j] > target:
                j -= 1
            elif sum2list[i] + sum2list[j] < target:
                i += 1
            else:
                potlist += [(sum2list[i],sum2list[j])]
                j -= 1
        ans = set()
        for tup in potlist:
            sumalist = sum2dict[tup[0]]
            sumblist = sum2dict[tup[1]]
            for suma in sumalist:
                for sumb in sumblist:
                    indset = set([suma[0],suma[1],sumb[0],sumb[1]])
                    if len(indset) < 4:
                        continue
                    ans.add(tuple(sorted([suma[2],suma[3],sumb[2],sumb[3]])))
        anslist = []
        for i in ans:
            anslist.append(list(i))
        return anslist
        
        
