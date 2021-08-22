'''
https://leetcode.com/problems/rectangle-area-ii/
'''
class Solution:
    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        def linesetadd(l0,l1):
            ln = []
            b0,b1 = l1[0],l1[1]
            i = 0
            while i < len(l0):
                a0,a1 = l0[i],l0[i+1]
                if a1 < b0:
                    ln += [a0,a1]
                elif a0 > b1:
                    ln += [b0,b1]
                    ln += l0[i:]
                    break
                else:
                    b0 = min(a0,b0)
                    b1 = max(a1,b1)
                i += 2
            if i == len(l0):
                ln += [b0,b1]
            return ln


        rectangles.sort()
        reclist = []
        for rec in rectangles:
            reclist += [[[rec[0],rec[2]],[rec[1],rec[3]]]]
        cover = [reclist[0]]
        for rec in reclist[1:]:
            newcover = []
            rx0,rx1 = rec[0]
            for cov in cover:
                cx0,cx1 = cov[0]
                if cx1 <= rx0 or cx0 >= rx1:  #rec与cov x轴不相交
                    newcover += [cov]
                else:
                    if cx0 < rx0:     
                        newcover += [[[cx0,rx0],cov[1]]]
                    newcover += [[[max(rx0,cx0),min(cx1,rx1)],linesetadd(cov[1],rec[1])]]
                    if cx1 > rx1:
                        newcover += [[[rx1,cx1],cov[1]]]
            if cx1 < rx1:
                newcover += [[[max(cx1,rx0),rx1],rec[1]]]
            cover = newcover
        ans = 0
        K = 10**9 + 7
        for rec in cover:
            ans += (rec[0][1]-rec[0][0]) *sum(rec[1][i] * (-1)**(i+1) for i in range(len(rec[1]))) % K
        return ans % K  
