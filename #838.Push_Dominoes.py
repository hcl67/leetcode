'''
https://leetcode.com/problems/push-dominoes/
'''
class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        l = len(dominoes)
        rd = [0] * l
        ld = [0] * l
        cf = 0
        c = 0
        for i in range(l):
            if cf == 0 and dominoes[i] == '.':
                continue
            elif dominoes[i] in ('R'):
                c = 0
                cf = 1
            elif cf == 1 and dominoes[i] == '.':
                c += 1
                rd[i] = c
            elif dominoes[i] == 'L':
                c = 0
                cf = 0
        cf = 0
        c = 0
        for i in range(l-1,-1,-1):
            if cf == 0 and dominoes[i] == '.':
                continue
            elif dominoes[i] in ('L'):
                c = 0
                cf = 1
            elif cf == 1 and dominoes[i] == '.':
                c -= 1
                ld[i] = c                
            elif dominoes[i] == 'R':
                c = 0
                cf = 0
        ans = ['.'] * l
        for i in range(l):
            if dominoes[i] in ('R','L'):
                ans[i] = dominoes[i]
            elif rd[i] == 0 and ld[i] != 0:
                ans[i] = 'L'
            elif rd[i] != 0 and ld[i] == 0:
                ans[i] = 'R'
            elif rd[i]+ld[i] < 0:
                ans[i] = 'R'
            elif rd[i]+ld[i] > 0:
                ans[i] = 'L'
        return ''.join(ans)

                
