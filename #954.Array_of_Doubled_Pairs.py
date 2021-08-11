'''
https://leetcode.com/problems/array-of-doubled-pairs/
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr = sorted(arr)

        tn = []
        tp = []

        for i in arr:
            if i < 0:
                if len(tn) == 0 or 2*i < tn[0]:
                    tn += [i]
                elif 2*i == tn[0]:
                    del tn[0]
                else:
                    return False
            else:
                if len(tn) > 0:
                    return False
                if len(tp) == 0 or i < 2 * tp[0]:
                    tp += [i]
                elif i == 2 * tp[0]:
                    del tp[0]
                else:
                    return False
        if len(tn) > 0 or len(tp) > 0:
            return False
        else:
            return True
