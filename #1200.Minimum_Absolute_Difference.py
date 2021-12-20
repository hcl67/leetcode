'''
https://leetcode.com/problems/minimum-absolute-difference/
'''
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        minabs = inf
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i] < minabs:
                minabs = arr[i+1]-arr[i]
                minlst = [[arr[i],arr[i+1]]]
            elif arr[i+1]-arr[i] == minabs:
                minlst += [[arr[i],arr[i+1]]]
        return minlst
        
        '''
        arrd = defaultdict(list)
        for i in range(len(arr)-1):
            arrd[arr[i+1]-arr[i]] += [[arr[i],arr[i+1]]]
        return arrd[min(arrd.keys())]
        
        '''
