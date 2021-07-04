'''
https://leetcode.com/problems/count-vowels-permutation/
'''
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        import numpy as np
        m = np.array([[0,1,0,0,0],[1,0,1,0,0],[1,1,0,1,1],[0,0,1,0,1],[1,0,0,0,0]])
        a = np.array([[1,1,1,1,1]])


        for k in range(n-1):
            a= np.matmul(a,m)
            for i in range(5):
                a[0,i] = a[0,i] % (10**9+7)
        return a.sum() % (10**9+7)

