'''
https://leetcode.com/problems/reduce-array-size-to-the-half/
'''
class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        from collections import defaultdict
        lenn = len(arr)
        arrdic = defaultdict(int)
        for i in range(lenn):
            arrdic[arr[i]] += 1
        vl = sorted(arrdic.values())[::-1]
        sum = 0
        for i in range(len(vl)):
            sum += vl[i]
            if sum*2>=lenn:
                break
        return i+1
