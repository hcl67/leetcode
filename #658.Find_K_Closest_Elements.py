'''
https://leetcode.com/problems/find-k-closest-elements/
'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        lenarr = len(arr)
        diffarr = [abs(i-x) for i in arr]
        mindiff = min(diffarr)
        indmin = diffarr.index(mindiff)
        upb = indmin
        lob = indmin
        for i in range(k-1):
            #print(lob,upb)
            if upb == lenarr-1:
                lob -= 1
            elif lob == 0:
                upb += 1
            elif abs(x-arr[lob-1]) <= abs(x-arr[upb+1]):
                lob -= 1
            else:
                upb += 1
        return arr[lob:upb+1]
