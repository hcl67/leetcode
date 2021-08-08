'''
https://leetcode.com/problems/rank-transform-of-a-matrix/
'''
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        d1 = len(matrix)
        d2 = len(matrix[0])

        # Tie dict

        def getdsu(p,dsu):
            if dsu[p[0]][p[1]] != (p[0],p[1]):
                dsu[p[0]][p[1]] = getdsu(dsu[p[0]][p[1]],dsu)
            return dsu[p[0]][p[1]]

        def undsu(p1,p2,dsu):
            p1 = getdsu(p1,dsu)
            p2 = getdsu(p2,dsu)
            if p1 == p2:
                return
            elif p1<p2:
                dsu[p2[0]][p2[1]] = p1
            else:
                dsu[p1[0]][p1[1]] = p2
            return



        tiedsu = [[(i,j) for j in range(d2)] for i in range(d1)]

        for i in range(d1):
            for j in range(d2):
                for k in range(i):
                    if matrix[k][j] == matrix[i][j]:
                        undsu((k,j),(i,j),tiedsu)
                        break
                for k in range(j):
                    if matrix[i][k] == matrix[i][j]:
                        undsu((i,k),(i,j),tiedsu)
                        break

        from collections import defaultdict

        tiedict = defaultdict(set)
        for i in range(d1):
            for j in range(d2):
                tiedict[getdsu((i,j),tiedsu)].add((i,j))

        ans = [[0 for j in range(d2)] for i in range(d1)]
        maxi = [0 for i in range(d1)]
        maxj = [0 for j in range(d2)]

        q = sorted(tiedict.keys(),key = lambda x:matrix[x[0]][x[1]])
        q = [tiedict[x] for x in q] 

        while len(q) > 0:
            curc = q[0]
            rk = 0
            for c in curc:
                c1,c2 = c
                rk = max(rk, maxi[c1], maxj[c2])
            for c in curc:
                c1,c2 = c
                ans[c1][c2] = rk + 1
                maxi[c1] = rk + 1
                maxj[c2] = rk + 1
            del q[0]
                
        return ans
