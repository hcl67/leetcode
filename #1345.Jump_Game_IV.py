'''
https://leetcode.com/problems/jump-game-iv/
'''
#BFS
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        invd = defaultdict(list)
        for i in range(len(arr)):
            invd[arr[i]].append(i)
        invd = dict(invd)
        ind = [len(arr)] * len(arr)
        i = 0
        q = [0]
        ind[0] = 0
        while ind[-1] == len(arr):
            i += 1
            nq = []
            for c in q:
                if c > 0 and ind[c-1] > i:
                    ind[c-1] = i
                    nq.append(c-1)
                if c < len(arr)-1 and ind[c+1] > i:
                    ind[c+1] = i
                    nq.append(c+1)
                if arr[c] in invd:
                    for eqc in invd[arr[c]]:
                        if ind[eqc] > i:
                            ind[eqc] = i
                            nq.append(eqc)
                    del invd[arr[c]]
            q = nq
        return ind[-1]
